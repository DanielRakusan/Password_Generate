from password_generator.language_pack import LANGUAGE_CS, LanguagePack
from password_generator.terminal import Terminal


def main():
    language_pack = LanguagePack(LANGUAGE_CS)
    terminal = Terminal(language_pack)
    terminal.change_language()
    terminal.run_loop()


if __name__ == "__main__":
    main()