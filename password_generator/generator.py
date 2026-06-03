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
        return [w.capitalize() for w in words]

    def _reverse(self, word: str) -> str:
        return word[::-1]

    def _random_special(self) -> str:
        return random.choice(self.SPECIAL_CHARS)

    def _random_separator(self) -> str:
        return random.choice(self.SEPARATORS)

    def _random_digits(self, n: int = 2) -> str:
        return "".join(random.choices(string.digits, k=n))

    # ========================================================================
    # Generování variant
    # ========================================================================

    def _variant_basic(self, words: list[str]) -> str:
        """keyword1keyword2keyword3"""
        return "".join(words)

    def _variant_capitalized(self, words: list[str]) -> str:
        """Keyword1Keyword2Keyword3"""
        return "".join(self._capitalize_all(words))

    def _variant_leet(self, words: list[str]) -> str:
        """k3yw0rd1K3yw0rd2"""
        caps = self._capitalize_all(words)
        parts = [self._leet(caps[0])] + caps[1:]
        return "".join(parts)

    def _variant_separator(self, words: list[str]) -> str:
        """Keyword1-Keyword2-Keyword3"""
        sep = self._random_separator()
        return sep.join(self._capitalize_all(words))

    def _variant_reversed(self, words: list[str]) -> str:
        """Keyword1Keyword2dryw3yek"""
        caps = self._capitalize_all(words)
        if len(caps) > 1:
            caps[-1] = self._reverse(caps[-1])
        else:
            caps[0] = self._reverse(caps[0])
        return "".join(caps)

    def _variant_with_number(self, words: list[str]) -> str:
        """Keyword1Keyword2 + 2 číslice"""
        return "".join(self._capitalize_all(words)) + self._random_digits()

    def _variant_special_wrap(self, words: list[str]) -> str:
        """!Keyword1Keyword2!"""
        sc = self._random_special()
        return sc + "".join(self._capitalize_all(words)) + sc

    def _variant_leet_number_special(self, words: list[str]) -> str:
        """k3yw0rd1K3yw0rd2 + číslice + special"""
        base = self._leet("".join(self._capitalize_all(words)))
        return base + self._random_digits() + self._random_special()

    def _variant_mixed(self, words: list[str]) -> str:
        """MiX — střídání velkých a malých písmen"""
        joined = "".join(words)
        result = ""
        for i, ch in enumerate(joined):
            result += ch.upper() if i % 2 == 0 else ch.lower()
        return result + self._random_special()

    def _variant_separator_leet(self, words: list[str]) -> str:
        """k3yw0rd1_K3yw0rd2_..."""
        sep = self._random_separator()
        return sep.join(self._leet(w.capitalize()) for w in words)

    # ========================================================================
    # Hlavní metoda
    # ========================================================================

    def generate(self, raw_input: str) -> list[str]:
        words = [w.strip() for w in raw_input.replace(",", " ").split() if w.strip()]

        if not words:
            return []

        variants = [
            self._variant_basic(words),
            self._variant_capitalized(words),
            self._variant_leet(words),
            self._variant_separator(words),
            self._variant_reversed(words),
            self._variant_with_number(words),
            self._variant_special_wrap(words),
            self._variant_leet_number_special(words),
            self._variant_mixed(words),
            self._variant_separator_leet(words),
        ]

        # odstraníme prázdné a duplicitní záznamy
        seen = set()
        result = []
        for v in variants:
            if v and v not in seen:
                seen.add(v)
                result.append(v)

        return result
