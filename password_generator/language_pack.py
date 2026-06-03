LANGUAGE_CS = "cs"
LANGUAGE_EN = "en"

LANGUAGE_TEXTS = {
    "cs":{
        # LanguagePack / jazykové hlášky
        "language_pack__unsupported_language": "Nepodporovaný jazyk",
        "language_pack__missing_key": "Chybějící klíč: {key}",

        #Terminal
        "menu__invalid_input": "Neplatná volba. Prosím, zkuste to znovu.",
        "menu__main_title": "Hlavní menu",
        "menu__input": "Zadejte číslo volby: ",
        "menu__input_not_valid": "Neplatná volba. Prosím, zkuste to znovu.",

        #Terminal main menu
        "menu_change_language": "Změnit jazyk",
        "menu__end_loop": "Ukončit program",

        #Terminal "menu__language"
        "menu__language": "Změnit jazyk",
        "menu__language_cs": "Čeština",
        "menu__language_en": "Angličtina",

        #Generator
        "menu__generate_password": "Generovat heslo",
        "generator__title": "Generátor hesel",
        "generator__enter_keywords": "Zadejte klíčová slova (oddělte čárkou nebo mezerou): ",
        "generator__no_keywords": "Nezadali jste žádná klíčová slova.",
        "generator__results_title": "Vygenerovaná hesla",
        "generator__copy_hint": "Vyberte heslo a zkopírujte jej.",
        "generator__back": "Zpět do hlavního menu",
        "generator__generate_again": "Generovat znovu"





    },
    "en":{
        # LanguagePack / jazykové hlášky
        "language_pack__unsupported_language": "Unsupported language",
        "language_pack__missing_key": "Missing key: {key}",

        #Terminal
        "menu__invalid_input": "Invalid option. Please try again.",
        "menu__main_title": "Main menu",
        "menu__input": "Choose an option: ",
        "menu__input_not_valid": "Invalid option. Please try again.",

        #Terminal main menu
        "menu_change_language": "Change language",
        "menu__end_loop": "Exit program",

        #Terminal "menu__language"
        "menu__language": "Change language",
        "menu__language_cs": "Czech",
        "menu__language_en": "English",

        #Generator
        "menu__generate_password": "Generate password",
        "generator__title": "Password generator",
        "generator__enter_keywords": "Enter keywords (separate with comma or space): ",
        "generator__no_keywords": "No keywords were entered.",
        "generator__results_title": "Generated passwords",
        "generator__copy_hint": "Select a password and copy it.",
        "generator__back": "Back to main menu",
        "generator__generate_again": "Generate again"

    }
}

class LanguagePack:
    def __init__(self, language = LANGUAGE_EN):
        self.language = language

    def changeLanguage(self, language):
        if language == LANGUAGE_EN:
            self.language = language
        elif language == LANGUAGE_CS:
            self.language = language
        else:
            raise ValueError(self.get_text("language_pack__unsupported_language"))

    def get_text(self, key):
        if self.language == LANGUAGE_EN:
            default_txt = f"{LANGUAGE_TEXTS[LANGUAGE_EN].get('language_pack__missing_key')} {key}"
        elif self.language == LANGUAGE_CS:
            default_txt = f"{LANGUAGE_TEXTS[LANGUAGE_CS].get('language_pack__missing_key')} {key}"

        return LANGUAGE_TEXTS[self.language].get(key, default_txt)



