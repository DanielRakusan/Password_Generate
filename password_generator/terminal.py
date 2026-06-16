import os

from password_generator.generator_screen import GeneratorScreen
from password_generator.language_texts import LANGUAGE_CS, LANGUAGE_EN


class Terminal:
    # ========================================================================
    # Inicializace a hlavní běh programu
    # ========================================================================

    def __init__(self, language_pack):
        self.language_pack    = language_pack
        self.generator_screen = GeneratorScreen(self)
        self.running          = True

    def run_loop(self):
        try:
            while self.running:
                self.menu(self.create_main_menu())
        except (KeyboardInterrupt, EOFError):
            self.clear_terminal()

    def end_loop(self):
        self.running = False

    # ========================================================================
    # Pomocné metody terminálu
    # ========================================================================

    def clear_terminal(self):
        if os.environ.get("TERM"):
            os.system("cls" if os.name == "nt" else "clear")

    def get_terminal_colors(self):
        return {
            "black":          "\033[30m",
            "red":            "\033[31m",
            "green":          "\033[32m",
            "yellow":         "\033[33m",
            "blue":           "\033[34m",
            "magenta":        "\033[35m",
            "cyan":           "\033[36m",
            "white":          "\033[37m",
            "bright_black":   "\033[90m",
            "bright_red":     "\033[91m",
            "bright_green":   "\033[92m",
            "bright_yellow":  "\033[93m",
            "bright_blue":    "\033[94m",
            "bright_magenta": "\033[95m",
            "bright_cyan":    "\033[96m",
            "bright_white":   "\033[97m",
            "reset":          "\033[0m",
        }

    def color_text(self, text, color=None):
        if color is None:
            return text

        colors = self.get_terminal_colors()

        if color not in colors:
            return text

        return f"{colors[color]}{text}{colors['reset']}"

    def get_text(self, key):
        return self.language_pack.get_text(key)

    # ========================================================================
    # Vstupní obrazovky
    # ========================================================================

    def ask_step(self, screen_title_key, step, total, title_key, prompt_key, hint_key):
        while True:
            self.clear_terminal()
            print(self.color_text(self.get_text(screen_title_key), "bright_cyan"))
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
            input(self.color_text(self.get_text("error__press_enter"), "bright_black"))

    def ask_number(self, step, total, max_number):
        while True:
            self.clear_terminal()
            print(self.color_text(self.get_text("recover__title"), "bright_cyan"))
            print()

            step_label = self.get_text("generator__step").format(step=step, total=total)
            print(self.color_text(step_label, "bright_black"))
            print(self.color_text(self.get_text("recover__step_4_title"), "bright_yellow"))
            print(self.color_text(self.get_text("recover__step_4_hint"), "bright_black"))
            print()

            prompt = self.get_text("recover__step_4_prompt").format(max=max_number)
            value = input(prompt).strip()

            if value.isdigit():
                number = int(value)
                if 1 <= number <= max_number:
                    return number

            print()
            error = self.get_text("recover__invalid_number").format(max=max_number)
            print(self.color_text(error, "bright_red"))
            input(self.color_text(self.get_text("error__press_enter"), "bright_black"))

    def show_results(self, passwords, alg_number, alg_name, platform, phrase, extra):
        self.clear_terminal()
        print(self.color_text(self.get_text("generator__title"), "bright_cyan"))
        print()
        print(self.color_text(self.get_text("generator__results_title"), "bright_yellow"))
        print()

        for i, pwd in enumerate(passwords, start=1):
            num = self.color_text(f"{i:2}.", "bright_black")
            print(f"  {num}  {self.color_text(pwd, 'bright_white')}")

        print()
        print(self.color_text(self.get_text("generator__copy_hint"), "bright_black"))
        print()
        print(self.color_text(self.get_text("generator__save_title"), "bright_yellow"))

        p_label  = self.get_text("generator__step_1_title")
        ph_label = self.get_text("generator__step_2_title")
        ex_label = self.get_text("generator__step_3_title")

        summary = f"  Alg. {alg_number} ({alg_name})  ·  {p_label}: {platform}  ·  {ph_label}: {phrase}  ·  {ex_label}: {extra}"
        print(self.color_text(summary, "bright_white"))
        print(self.color_text(self.get_text("generator__save_number_hint"), "bright_black"))
        print()

    def show_password(self, number, password):
        self.clear_terminal()
        print(self.color_text(self.get_text("recover__title"), "bright_cyan"))
        print()
        print(self.color_text(self.get_text("recover__result_title").format(number=number), "bright_yellow"))
        print()
        print(f"  {self.color_text(password, 'bright_white')}")
        print()
        print(self.color_text(self.get_text("generator__copy_hint"), "bright_black"))
        print()

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
                "0": {
                    "text_key": "menu__back",
                    "action": lambda: None,
                    "args": (),
                    "color": "bright_black",
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
                    "action": self.generator_screen.run,
                    "args": (),
                    "color": "bright_green",
                },
                "2": {
                    "text_key": "menu__recover_password",
                    "action": self.generator_screen.run_by_number,
                    "args": (),
                    "color": "bright_blue",
                },
                "3": {
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

    def menu(self, menu_items, clear=True):
        first_render = True
        while True:
            try:
                if clear or not first_render:
                    self.clear_terminal()
                first_render = False

                print(self.get_text(menu_items["title_key"]))

                for key in menu_items["options"]:
                    option = menu_items["options"][key]
                    text = self.color_text(
                        self.get_text(option["text_key"]),
                        option.get("color"),
                    )
                    print(f"{key}: {text} ")

                print()
                volba = input(self.get_text("menu__input")).strip()

                if volba not in menu_items["options"]:
                    raise ValueError()

                option = menu_items["options"][volba]
                return option.get("action", lambda: None)(*option.get("args", ()))

            except (ValueError, KeyboardInterrupt, EOFError):
                print()
                print(self.color_text(self.get_text("menu__invalid_input"), "bright_red"))
                input(self.color_text(self.get_text("error__press_enter"), "bright_black"))
