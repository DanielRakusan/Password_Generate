from password_generator.language_texts import LANGUAGE_TEXTS, LANGUAGE_CS, LANGUAGE_EN


class LanguagePack:
    # ========================================================================
    # Inicializace
    # ========================================================================

    def __init__(self, language: str = LANGUAGE_EN):
        self.language = language

    # ========================================================================
    # Přepínání jazyka
    # ========================================================================

    def changeLanguage(self, language: str) -> None:
        if language not in (LANGUAGE_CS, LANGUAGE_EN):
            raise ValueError(self.get_text("language_pack__unsupported_language"))
        self.language = language

    # ========================================================================
    # Získání textu
    # ========================================================================

    def get_text(self, key: str) -> str:
        missing = LANGUAGE_TEXTS[self.language].get("language_pack__missing_key", "Missing key: {key}")
        return LANGUAGE_TEXTS[self.language].get(key, missing.format(key=key))
