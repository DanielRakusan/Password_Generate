from password_generator.generator import PasswordGenerator, _VARIANTS


class GeneratorScreen:
    # ========================================================================
    # Inicializace
    # ========================================================================

    def __init__(self, terminal, generator: PasswordGenerator):
        self.terminal  = terminal
        self.generator = generator

    # ========================================================================
    # Vstupní kroky
    # ========================================================================

    def _ask_step(self, step: int, total: int, title_key: str, prompt_key: str, hint_key: str) -> str:
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

    # ========================================================================
    # Zobrazení výsledků
    # ========================================================================

    def _show_results(self, passwords: list[str]) -> None:
        t = self.terminal
        t.clear_terminal()
        print(t.color_text(t.get_text("generator__title"), "bright_cyan"))
        print()
        print(t.color_text(t.get_text("generator__results_title"), "bright_yellow"))
        print()

        for i, (pwd, (length, charset)) in enumerate(zip(passwords, _VARIANTS), start=1):
            has_special = charset not in ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
                                          "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz23456789")
            tag = f"{length} zn." + (" + spec." if has_special else "")
            tag_colored = t.color_text(f"[{tag}]", "bright_black")
            pwd_colored  = t.color_text(pwd, "bright_white")
            num_colored  = t.color_text(f"{i:2}.", "bright_black")
            print(f"  {num_colored} {tag_colored}  {pwd_colored}")

        print()
        print(t.color_text(t.get_text("generator__copy_hint"), "bright_black"))
        print()

    # ========================================================================
    # Hlavní smyčka
    # ========================================================================

    def run(self) -> None:
        t = self.terminal
        while True:
            platform = self._ask_step(1, 3, "generator__step_1_title", "generator__step_1_prompt", "generator__step_1_hint")
            phrase   = self._ask_step(2, 3, "generator__step_2_title", "generator__step_2_prompt", "generator__step_2_hint")
            extra    = self._ask_step(3, 3, "generator__step_3_title", "generator__step_3_prompt", "generator__step_3_hint")

            passwords = self.generator.generate(platform, phrase, extra)
            self._show_results(passwords)

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
