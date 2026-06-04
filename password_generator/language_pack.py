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



