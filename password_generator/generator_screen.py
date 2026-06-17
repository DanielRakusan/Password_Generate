from password_generator.generator         import PasswordGenerator
from password_generator.generator_sha512  import PasswordGeneratorSHA512
from password_generator.generator_md5     import PasswordGeneratorMD5
from password_generator.generator_sha1    import PasswordGeneratorSHA1
from password_generator.generator_caesar  import PasswordGeneratorCaesar
from password_generator.generator_enigma  import PasswordGeneratorEnigma


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
                    "action": lambda: (1, "SHA-256", PasswordGenerator()),
                    "args": (),
                },
                "2": {
                    "text_key": "algorithm__sha512",
                    "action": lambda: (2, "SHA-512", PasswordGeneratorSHA512()),
                    "args": (),
                },
                "3": {
                    "text_key": "algorithm__md5",
                    "action": lambda: (3, "MD5", PasswordGeneratorMD5()),
                    "args": (),
                },
                "4": {
                    "text_key": "algorithm__sha1",
                    "action": lambda: (4, "SHA-1", PasswordGeneratorSHA1()),
                    "args": (),
                },
                "5": {
                    "text_key": "algorithm__caesar",
                    "action": lambda: (5, "Caesar", PasswordGeneratorCaesar()),
                    "args": (),
                },
                "6": {
                    "text_key": "algorithm__enigma",
                    "action": lambda: (6, "Enigma", PasswordGeneratorEnigma()),
                    "args": (),
                },
                "0": {
                    "text_key": "menu__back",
                    "action": lambda: None,
                    "args": (),
                    "color": "bright_black",
                },
            },
        }

        return t.menu(algorithm_menu)

    # ========================================================================
    # Generování hesel
    # ========================================================================

    def run(self):
        t = self.terminal

        while True:
            result = self._ask_algorithm()
            if result is None:
                return
            alg_number, alg_name, generator = result

            enigma_key = None
            if alg_name == "Enigma":
                ri, rii, riii, ref = generator.build_rotors()
                config = t.ask_enigma_config(2, 5, ri, rii, riii, ref)
                if config is None:
                    continue
                enigma_key = config if config else None
                if enigma_key:
                    generator.enigma_key = enigma_key
                    ri, rii, riii, ref = generator.build_rotors(enigma_key)
                    t.show_enigma_custom_tables(2, 5, ri, rii, riii, ref)
                platform = t.ask_step("generator__title", 3, 5, "generator__step_1_title", "generator__step_1_prompt", "generator__step_1_hint")
                phrase   = t.ask_step("generator__title", 4, 5, "generator__step_2_title", "generator__step_2_prompt", "generator__step_2_hint")
                extra    = t.ask_step("generator__title", 5, 5, "generator__step_3_title", "generator__step_3_prompt", "generator__step_3_hint")
            else:
                platform = t.ask_step("generator__title", 2, 4, "generator__step_1_title", "generator__step_1_prompt", "generator__step_1_hint")
                phrase   = t.ask_step("generator__title", 3, 4, "generator__step_2_title", "generator__step_2_prompt", "generator__step_2_hint")
                extra    = t.ask_step("generator__title", 4, 4, "generator__step_3_title", "generator__step_3_prompt", "generator__step_3_hint")

            passwords = generator.generate(platform, phrase, extra)
            t.show_results(passwords, alg_number, alg_name, platform, phrase, extra, enigma_key)

            again_menu = {
                "title_key": "generator__title",
                "options": {
                    "1": {
                        "text_key": "generator__generate_again",
                        "action": lambda: "again",
                        "args": (),
                        "color": "bright_green",
                    },
                    "0": {
                        "text_key": "menu__back",
                        "action": lambda: "back",
                        "args": (),
                        "color": "bright_black",
                    },
                },
            }

            result = t.menu(again_menu, clear=False)
            if result == "back":
                return

    # ========================================================================
    # Zobrazení hesla podle čísla
    # ========================================================================

    def run_by_number(self):
        t = self.terminal

        while True:
            result = self._ask_algorithm()
            if result is None:
                return
            alg_number, alg_name, generator = result

            if alg_name == "Enigma":
                ri, rii, riii, ref = generator.build_rotors()
                config = t.ask_enigma_config(2, 6, ri, rii, riii, ref)
                if config is None:
                    continue
                enigma_key = config if config else None
                if enigma_key:
                    generator.enigma_key = enigma_key
                    ri, rii, riii, ref = generator.build_rotors(enigma_key)
                    t.show_enigma_custom_tables(2, 6, ri, rii, riii, ref)
                platform = t.ask_step("recover__title", 3, 6, "generator__step_1_title", "generator__step_1_prompt", "generator__step_1_hint")
                phrase   = t.ask_step("recover__title", 4, 6, "generator__step_2_title", "generator__step_2_prompt", "generator__step_2_hint")
                extra    = t.ask_step("recover__title", 5, 6, "generator__step_3_title", "generator__step_3_prompt", "generator__step_3_hint")
                number   = t.ask_number(6, 6, len(generator.VARIANTS))
            else:
                platform = t.ask_step("recover__title", 2, 5, "generator__step_1_title", "generator__step_1_prompt", "generator__step_1_hint")
                phrase   = t.ask_step("recover__title", 3, 5, "generator__step_2_title", "generator__step_2_prompt", "generator__step_2_hint")
                extra    = t.ask_step("recover__title", 4, 5, "generator__step_3_title", "generator__step_3_prompt", "generator__step_3_hint")
                number   = t.ask_number(5, 5, len(generator.VARIANTS))

            password = generator.generate_one(platform, phrase, extra, number)
            t.show_password(number, password)

            again_menu = {
                "title_key": "recover__title",
                "options": {
                    "1": {
                        "text_key": "generator__generate_again",
                        "action": lambda: "again",
                        "args": (),
                        "color": "bright_green",
                    },
                    "0": {
                        "text_key": "menu__back",
                        "action": lambda: "back",
                        "args": (),
                        "color": "bright_black",
                    },
                },
            }

            result = t.menu(again_menu, clear=False)
            if result == "back":
                return
