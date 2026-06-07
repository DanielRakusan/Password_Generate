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
        while self.running:
            self.menu(self.create_main_menu())

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

    def menu(self, menu_items):
        while True:
            try:
                self.clear_terminal()

                print(self.get_text(menu_items["title_key"]))

                for key in menu_items["options"]:
                    option = menu_items["options"][key]
                    text = self.color_text(
                        self.get_text(option["text_key"]),
                        option.get("color"),
                    )
                    print(f"{key}: {text} ")

                print()
                volba = input(self.get_text("menu__input"))

                if volba not in menu_items["options"]:
                    raise ValueError(self.get_text("menu__input_not_valid"))

                option = menu_items["options"][volba]
                self.clear_terminal()
                return option.get("action", lambda: None)(*option.get("args", ()))

            except ValueError:
                print(self.get_text("menu__invalid_input"))
