import os

from password_generator.generator import PasswordGenerator
from password_generator.language_pack import LANGUAGE_EN, LANGUAGE_CS


class Terminal:
    # ========================================================================
    # Inicializace a hlavní běh programu
    # ========================================================================

    def __init__(self, language_pack):
        self.language_pack = language_pack
        self.generator = PasswordGenerator()
        self.running = True

    def run_loop(self):
        while self.running:
            self.menu(self.create_main_menu())

    def end_loop(self):
        self.running = False

    # ========================================================================
    # Pomocné metody terminálu
    # ========================================================================

    def clear_terminal(self):
        # Vyčištění terminálu podle operačního systému.
        if os.environ.get("TERM"):
            os.system("cls" if os.name == "nt" else "clear")

    def get_terminal_colors(self):
        # Vrací dostupné ANSI barvy pro obarvení textu v terminálu.
        return {
            "black": "\033[30m",
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "white": "\033[37m",
            "bright_black": "\033[90m",
            "bright_red": "\033[91m",
            "bright_green": "\033[92m",
            "bright_yellow": "\033[93m",
            "bright_blue": "\033[94m",
            "bright_magenta": "\033[95m",
            "bright_cyan": "\033[96m",
            "bright_white": "\033[97m",
            "reset": "\033[0m",
        }

    def color_text(self, text, color=None):
        # Vrátí obarvený text, pokud je zadaná platná barva.
        if color is None:
            return text

        colors = self.get_terminal_colors()

        if color not in colors:
            return text

        color_code = colors[color]
        reset_code = colors["reset"]

        return f"{color_code}{text}{reset_code}"

    def get_text(self, key):
        # Vrátí text podle aktuálně nastaveného jazyka.
        return self.language_pack.get_text(key)

    # ========================================================================
    # Generátor hesel
    # ========================================================================

    def _generator_ask_step(self, step: int, total: int, title_key: str, prompt_key: str, hint_key: str) -> str:
        while True:
            self.clear_terminal()
            print(self.color_text(self.get_text("generator__title"), "bright_cyan"))
            print()

            step_label = self.get_text("generator__step").format(step=step, total=total)
            print(self.color_text(step_label, "bright_black"))
            print(self.color_text(self.get_text(title_key), "bright_yellow"))
            print(self.color_text(self.get_text(hint_key), "bright_black"))
            print()

            value = input(self.get_text(prompt_key)).strip()

            if value:
                return value

            print()
            print(self.color_text(self.get_text("generator__no_input"), "bright_red"))
            input()

    def run_generator(self):
        while True:
            platform = self._generator_ask_step(
                1, 3,
                "generator__step_1_title",
                "generator__step_1_prompt",
                "generator__step_1_hint",
            )
            phrase = self._generator_ask_step(
                2, 3,
                "generator__step_2_title",
                "generator__step_2_prompt",
                "generator__step_2_hint",
            )
            extra = self._generator_ask_step(
                3, 3,
                "generator__step_3_title",
                "generator__step_3_prompt",
                "generator__step_3_hint",
            )

            passwords = self.generator.generate(platform, phrase, extra)

            self.clear_terminal()
            print(self.color_text(self.get_text("generator__title"), "bright_cyan"))
            print()
            print(self.color_text(self.get_text("generator__results_title"), "bright_yellow"))
            print()

            for i, pwd in enumerate(passwords, start=1):
                print(f"  {self.color_text(str(i) + '.', 'bright_black')} {self.color_text(pwd, 'bright_white')}")

            print()
            print(self.color_text(self.get_text("generator__copy_hint"), "bright_black"))
            print()

            again_menu = {
                "title_key": "generator__title",
                "options": {
                    "1": {
                        "text_key": "generator__generate_again",
                        "action": lambda: "again",
                        "args": (),
                        "color": "bright_green",
                    },
                    "2": {
                        "text_key": "generator__back",
                        "action": lambda: "back",
                        "args": (),
                        "color": "bright_red",
                    },
                },
            }

            result = self.menu(again_menu)
            if result == "back":
                return

    # ========================================================================
    # Sestavení menu
    # ========================================================================

    def change_language(self):
        change_language = {
            "title_key": "menu__language",
            "options": {
                "1": {
                    "text_key": "menu__language_cs",
                    "action": self.language_pack.changeLanguage,
                    "args": (LANGUAGE_CS,),
                    "color": "bright_blue",
                },
                "2": {
                    "text_key": "menu__language_en",
                    "action": self.language_pack.changeLanguage,
                    "args": (LANGUAGE_EN,),
                    "color": "bright_red",
                },
            },
        }

        self.menu(change_language)

    def create_main_menu(self):
        return {
            "title_key": "menu__main_title",
            "options": {
                "1": {
                    "text_key": "menu__generate_password",
                    "action": self.run_generator,
                    "args": (),
                    "color": "bright_green",
                },
                "2": {
                    "text_key": "menu_change_language",
                    "action": self.change_language,
                    "args": (),
                },
                "5": {
                    "text_key": "menu__end_loop",
                    "action": self.end_loop,
                    "args": (),
                    "color": "bright_red",
                },
            },
        }

    # ========================================================================
    # Vykreslení a ovládání menu
    # ========================================================================

    def menu(self, menu_items):
        # Vykreslí předané menu, načte volbu a spustí odpovídající akci.
        while True:
            try:
                self.clear_terminal()

                print(self.get_text(menu_items["title_key"]))

                for menu_item in menu_items["options"]:
                    text_key = menu_items["options"][menu_item]["text_key"]
                    text = self.color_text(
                        self.get_text(text_key),
                        menu_items["options"][menu_item].get("color"),
                    )

                    print(f"{menu_item}: {text} ")

                print()
                volba = input(self.get_text("menu__input"))

                if volba not in menu_items["options"]:
                    raise ValueError(
                        self.get_text("menu__input_not_valid")
                    )

                action = menu_items["options"][volba].get(
                    "action",
                    lambda: self.get_text("menu__input_not_valid"),
                )
                args = menu_items["options"][volba].get("args", ())

                self.clear_terminal()
                return action(*args)

            except ValueError:
                print(self.get_text("menu__invalid_input"))

