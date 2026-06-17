LANGUAGE_CS = "cs"
LANGUAGE_EN = "en"

LANGUAGE_TEXTS = {
    "cs": {
        # LanguagePack / jazykové hlášky
        "language_pack__unsupported_language": "Nepodporovaný jazyk",
        "language_pack__missing_key": "Chybějící klíč: {key}",

        # Terminal
        "menu__invalid_input": "Neplatná volba. Prosím, zkuste to znovu.",
        "menu__main_title": "Hlavní menu",
        "menu__input": "Zadejte číslo volby: ",
        "menu__input_not_valid": "Neplatná volba. Prosím, zkuste to znovu.",

        # Hlavní menu
        "menu_change_language": "Změnit jazyk",
        "menu__end_loop": "Ukončit program",
        "menu__back": "Zpět",
        "error__press_enter": "Stiskněte Enter pro pokračování...",

        # Výběr jazyka
        "menu__language": "Změnit jazyk",
        "menu__language_cs": "Čeština",
        "menu__language_en": "Angličtina",

        # Generátor
        "menu__generate_password": "Generovat heslo",
        "generator__title": "Generátor hesel",
        "generator__step": "Krok {step} ze {total}",
        "generator__step_1_title": "Platforma",
        "generator__step_1_prompt": "Na jaké platformě se heslo používá? ",
        "generator__step_1_hint": "(např. Gmail, Facebook, Banka...)",
        "generator__step_2_title": "Fráze",
        "generator__step_2_prompt": "Zadejte větu nebo frázi, kterou si zapamatujete: ",
        "generator__step_2_hint": "(např. MamRadPsy, OblibenaMista...)",
        "generator__step_3_title": "Extra",
        "generator__step_3_prompt": "Zadejte číslo nebo slovo navíc: ",
        "generator__step_3_hint": "(např. rok narození, oblíbené číslo, přezdívka...)",
        "generator__no_input": "Vstup nemůže být prázdný. Zkuste to znovu.",
        "generator__results_title": "Vygenerovaná hesla",
        "generator__copy_hint": "Vyberte heslo a zkopírujte jej.",
        "generator__note_hint": "Poznamenejte si: algoritmus č.{alg} + číslo hesla!",
        "generator__save_title": "Uložte si (přesně jak jste zadali):",
        "generator__save_number_hint": "Číslo hesla: ___  (dopište číslo hesla, které si vyberete)",

        # Výběr algoritmu
        "algorithm__title": "Výběr algoritmu hešování",
        "algorithm__sha256": "SHA-256  (doporučeno)",
        "algorithm__sha512": "SHA-512",
        "algorithm__md5": "MD5",
        "algorithm__sha1": "SHA-1",
        "algorithm__caesar": "Caesar",
        "algorithm__enigma": "Enigma",
        "generator__back": "Zpět do hlavního menu",
        "generator__generate_again": "Generovat znovu",

        # Enigma konfigurace rotorů
        "enigma__config_default": "Historické tabulky — Wehrmacht Enigma (výchozí)",
        "enigma__config_custom": "Vlastní tabulky — vygenerovány z klíče",
        "enigma__config_input": "Vlastní klíč (Enter = použít historické tabulky): ",
        "enigma__key_warning": "POZOR: Zapište si klíč! Bez něj heslo nevygenerujete znovu.",
        "enigma__key_label": "Enigma klíč: {key}",

        # Zobrazení hesla podle čísla
        "menu__recover_password": "Zobrazit heslo podle čísla",
        "recover__title": "Zobrazit heslo",
        "recover__step_4_title": "Číslo hesla",
        "recover__step_4_prompt": "Zadejte číslo hesla (1-{max}): ",
        "recover__step_4_hint": "(číslo, které jste si poznamenali při generování)",
        "recover__result_title": "Vaše heslo č. {number}",
        "recover__invalid_number": "Neplatné číslo. Zadejte číslo od 1 do {max}.",
    },
    "en": {
        # LanguagePack / jazykové hlášky
        "language_pack__unsupported_language": "Unsupported language",
        "language_pack__missing_key": "Missing key: {key}",

        # Terminal
        "menu__invalid_input": "Invalid option. Please try again.",
        "menu__main_title": "Main menu",
        "menu__input": "Choose an option: ",
        "menu__input_not_valid": "Invalid option. Please try again.",

        # Hlavní menu
        "menu_change_language": "Change language",
        "menu__end_loop": "Exit program",
        "menu__back": "Back",
        "error__press_enter": "Press Enter to continue...",

        # Výběr jazyka
        "menu__language": "Change language",
        "menu__language_cs": "Czech",
        "menu__language_en": "English",

        # Generátor
        "menu__generate_password": "Generate password",
        "generator__title": "Password generator",
        "generator__step": "Step {step} of {total}",
        "generator__step_1_title": "Platform",
        "generator__step_1_prompt": "Which platform is this password for? ",
        "generator__step_1_hint": "(e.g. Gmail, Facebook, Bank...)",
        "generator__step_2_title": "Phrase",
        "generator__step_2_prompt": "Enter a sentence or phrase you will remember: ",
        "generator__step_2_hint": "(e.g. ILoveDogs, FavoritePlaces...)",
        "generator__step_3_title": "Extra",
        "generator__step_3_prompt": "Enter a number or word as extra: ",
        "generator__step_3_hint": "(e.g. birth year, favourite number, nickname...)",
        "generator__no_input": "Input cannot be empty. Please try again.",
        "generator__results_title": "Generated passwords",
        "generator__copy_hint": "Select a password and copy it.",
        "generator__note_hint": "Note down: algorithm no.{alg} + password number!",
        "generator__save_title": "Save (exactly as you entered):",
        "generator__save_number_hint": "Password no.: ___  (fill in the number you choose)",

        # Algorithm selection
        "algorithm__title": "Hashing algorithm",
        "algorithm__sha256": "SHA-256  (recommended)",
        "algorithm__sha512": "SHA-512",
        "algorithm__md5": "MD5",
        "algorithm__sha1": "SHA-1",
        "algorithm__caesar": "Caesar",
        "algorithm__enigma": "Enigma",
        "generator__back": "Back to main menu",
        "generator__generate_again": "Generate again",

        # Enigma rotor configuration
        "enigma__config_default": "Historical tables — Wehrmacht Enigma (default)",
        "enigma__config_custom": "Custom tables — generated from your key",
        "enigma__config_input": "Custom key (Enter = use historical tables): ",
        "enigma__key_warning": "WARNING: Write down your key! Without it you cannot regenerate the password.",
        "enigma__key_label": "Enigma key: {key}",

        # Show password by number
        "menu__recover_password": "Show password by number",
        "recover__title": "Show password",
        "recover__step_4_title": "Password number",
        "recover__step_4_prompt": "Enter password number (1-{max}): ",
        "recover__step_4_hint": "(the number you noted down when generating)",
        "recover__result_title": "Your password no. {number}",
        "recover__invalid_number": "Invalid number. Enter a number from 1 to {max}.",
    },
}
