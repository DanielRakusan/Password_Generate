import random
import string


class PasswordGenerator:
    # ========================================================================
    # Tabulky pro transformace
    # ========================================================================

    LEET_MAP = {
        "a": "@", "e": "3", "i": "1", "o": "0",
        "s": "$", "t": "7", "b": "8", "g": "9",
    }

    SPECIAL_CHARS = ["!", "@", "#", "$", "%", "&", "*", "?"]
    SEPARATORS    = ["-", "_", ".", "|"]

    # ========================================================================
    # Pomocné transformace
    # ========================================================================

    def _leet(self, word: str) -> str:
        return "".join(self.LEET_MAP.get(c, c) for c in word.lower())

    def _capitalize_all(self, words: list[str]) -> list[str]:
        return [(w[0].upper() + w[1:]) if w else w for w in words]

    def _reverse(self, word: str) -> str:
        return word[::-1]

    def _initials(self, words: list[str]) -> str:
        return "".join(w[0].upper() for w in words if w)

    def _random_special(self) -> str:
        return random.choice(self.SPECIAL_CHARS)

    def _random_separator(self) -> str:
        return random.choice(self.SEPARATORS)

    def _random_digits(self, n: int = 2) -> str:
        return "".join(random.choices(string.digits, k=n))

    # ========================================================================
    # Generování variant ze 3 klíčových vstupů
    # ========================================================================

    def generate(self, platform: str, phrase: str, extra: str) -> list[str]:
        plt   = platform.strip()
        words = [w.strip() for w in phrase.replace(",", " ").split() if w.strip()]
        ext   = extra.strip()

        if not plt or not words or not ext:
            return []

        plt_cap      = plt.capitalize()
        plt_initial  = plt[0].upper()
        plt_leet     = self._leet(plt_cap)
        phr_cap      = "".join(self._capitalize_all(words))
        phr_leet     = self._leet(phr_cap)
        phr_initials = self._initials(words)
        sep          = self._random_separator()

        variants = [
            # Platform + phrase + extra
            plt_cap + phr_cap + ext,
            # Platform initial + sep + phrase + sep + extra
            plt_initial + sep + phr_cap + sep + ext,
            # Leet na platformě + phrase + extra
            plt_leet + phr_cap + ext,
            # Phrase + extra + special (platforma skryta)
            phr_cap + ext + self._random_special(),
            # Initials platformy + initials phrase + extra
            plt_initial + phr_initials + ext,
            # Phrase initials + sep + platform + sep + extra
            phr_initials + sep + plt_cap + sep + ext,
            # Leet na phrase + extra + initial platformy
            phr_leet + ext + plt_initial,
            # Platform + # + phrase + # + extra
            plt_cap + "#" + phr_cap + "#" + ext,
            # Obrácené extra + obrácená platforma + sep + phrase
            self._reverse(ext) + self._reverse(plt_cap) + sep + phr_cap,
            # Platform + phrase initials + extra + special
            plt_cap + phr_initials + ext + self._random_special(),
        ]

        seen = set()
        result = []
        for v in variants:
            if v and v not in seen:
                seen.add(v)
                result.append(v)

        return result
