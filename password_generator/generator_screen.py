from password_generator.generator         import PasswordGenerator
from password_generator.generator_sha512  import PasswordGeneratorSHA512
from password_generator.generator_md5     import PasswordGeneratorMD5
from password_generator.generator_sha1    import PasswordGeneratorSHA1
from password_generator.generator_caesar  import PasswordGeneratorCaesar


class GeneratorScreen:
    # ========================================================================
    # Inicializace
    # ========================================================================

    def __init__(self, terminal):
        self.terminal = terminal

    # ========================================================================
    # Výběr algoritmu
    # ========================================================================

    def _ask_algorithm(self):
        t = self.terminal

        algorithm_menu = {
            "title_key": "algorithm__title",
            "options": {
                "1": {
                    "text_key": "algorithm__sha256",
                    "action": lambda: (1, PasswordGenerator()),
                    "args": (),
                },
                "2": {
                    "text_key": "algorithm__sha512",
                    "action": lambda: (2, PasswordGeneratorSHA512()),
                    "args": (),
                },
                "3": {
                    "text_key": "algorithm__md5",
                    "action": lambda: (3, PasswordGeneratorMD5()),
                    "args": (),
                },
                "4": {
                    "text_key": "algorithm__sha1",
                    "action": lambda: (4, PasswordGeneratorSHA1()),
                    "args": (),
                },
                "5": {
                    "text_key": "algorithm__caesar",
                    "action": lambda: (5, PasswordGeneratorCaesar()),
                    "args": (),
                },
            },
        }

        return t.menu(algorithm_menu)

    # ========================================================================
    # Vstupní kroky
    # ========================================================================

    def _ask_step(self, step, total, title_key, prompt_key, hint_key):
        # Zobrazí jeden krok průvodce a vrátí zadaný vstup.
        t = self.terminal

        while True:
            t.clear_terminal()
            print(t.color_text(t.get_text("generator__title"), "bright_cyan"))
            print()

            step_label = t.get_text("generator__step").format(step=step, total=total)
            print(t.color_text(step_label, "bright_black"))
            print(t.color_text(t.get_text(title_key), "bright_yellow"))
            print(t.color_text(t.get_text(hint_key), "bright_black"))
            print()

            value = input(t.get_text(prompt_key)).strip()

            if value:
                return value

            print()
            print(t.color_text(t.get_text("generator__no_input"), "bright_red"))
            input()

    def _ask_number(self, step, total, max_number):
        t = self.terminal

        while True:
            t.clear_terminal()
            print(t.color_text(t.get_text("recover__title"), "bright_cyan"))
            print()

            step_label = t.get_text("generator__step").format(step=step, total=total)
            print(t.color_text(step_label, "bright_black"))
            print(t.color_text(t.get_text("recover__step_4_title"), "bright_yellow"))
            print(t.color_text(t.get_text("recover__step_4_hint"), "bright_black"))
            print()

            prompt = t.get_text("recover__step_4_prompt").format(max=max_number)
            value = input(prompt).strip()

            if value.isdigit():
                number = int(value)
                if 1 <= number <= max_number:
                    return number

            print()
            error = t.get_text("recover__invalid_number").format(max=max_number)
            print(t.color_text(error, "bright_red"))
            input()

    # ========================================================================
    # Zobrazení výsledků
    # ========================================================================

    def _show_results(self, passwords, alg_number):
        t = self.terminal

        t.clear_terminal()
        print(t.color_text(t.get_text("generator__title"), "bright_cyan"))
        print()
        print(t.color_text(t.get_text("generator__results_title"), "bright_yellow"))
        print()

        for i, pwd in enumerate(passwords, start=1):
            num = t.color_text(f"{i:2}.", "bright_black")
            print(f"  {num}  {t.color_text(pwd, 'bright_white')}")

        print()
        print(t.color_text(t.get_text("generator__copy_hint"), "bright_black"))
        print(t.color_text(t.get_text("generator__note_hint").format(alg=alg_number), "bright_yellow"))
        print()

    # ========================================================================
    # Generování hesel
    # ========================================================================

    def run(self):
        t = self.terminal

        while True:
            alg_number, generator = self._ask_algorithm()

            platform = self._ask_step(2, 4, "generator__step_1_title", "generator__step_1_prompt", "generator__step_1_hint")
            phrase   = self._ask_step(3, 4, "generator__step_2_title", "generator__step_2_prompt", "generator__step_2_hint")
            extra    = self._ask_step(4, 4, "generator__step_3_title", "generator__step_3_prompt", "generator__step_3_hint")

            passwords = generator.generate(platform, phrase, extra)
            self._show_results(passwords, alg_number)

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

            result = t.menu(again_menu)
            if result == "back":
                return

    # ========================================================================
    # Zobrazení hesla podle čísla
    # ========================================================================

    def run_by_number(self):
        t = self.terminal

        while True:
            alg_number, generator = self._ask_algorithm()

            platform   = self._ask_step(2, 5, "generator__step_1_title", "generator__step_1_prompt", "generator__step_1_hint")
            phrase     = self._ask_step(3, 5, "generator__step_2_title", "generator__step_2_prompt", "generator__step_2_hint")
            extra      = self._ask_step(4, 5, "generator__step_3_title", "generator__step_3_prompt", "generator__step_3_hint")
            number     = self._ask_number(5, 5, len(generator.VARIANTS))

            password = generator.generate_one(platform, phrase, extra, number)

            t.clear_terminal()
            print(t.color_text(t.get_text("recover__title"), "bright_cyan"))
            print()
            print(t.color_text(t.get_text("recover__result_title").format(number=number), "bright_yellow"))
            print()
            print(f"  {t.color_text(password, 'bright_white')}")
            print()
            print(t.color_text(t.get_text("generator__copy_hint"), "bright_black"))
            print()

            again_menu = {
                "title_key": "recover__title",
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

            result = t.menu(again_menu)
            if result == "back":
                return
