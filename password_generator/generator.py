import hashlib


CHARSET_FULL  = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*?"
CHARSET_ALNUM = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
CHARSET_SAFE  = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz23456789"

_UPPER   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_LOWER   = "abcdefghijklmnopqrstuvwxyz"
_DIGITS  = "0123456789"
_SPECIAL = "!@#$%&*?"

# (délka, charset)
_VARIANTS = [
    (16, CHARSET_FULL),
    (12, CHARSET_FULL),
    (20, CHARSET_FULL),
    (16, CHARSET_ALNUM),
    (20, CHARSET_ALNUM),
    (12, CHARSET_ALNUM),
    (16, CHARSET_SAFE),
    (24, CHARSET_ALNUM),
    (18, CHARSET_FULL),
    (32, CHARSET_ALNUM),
]


class PasswordGenerator:
    # ========================================================================
    # Derivace hesla — deterministická
    # ========================================================================

    def _raw_bytes(self, platform: str, phrase: str, extra: str, variant_idx: int) -> bytes:
        seed = f"{platform}|{phrase}|{extra}|{variant_idx}".encode("utf-8")
        out = b""
        current = seed
        while len(out) < 64:
            current = hashlib.sha256(current).digest()
            out += current
        return out

    def _derive(self, platform: str, phrase: str, extra: str, idx: int, length: int, charset: str) -> str:
        raw = self._raw_bytes(platform, phrase, extra, idx)
        uses_special = charset == CHARSET_FULL

        # Zaručíme přítomnost každého typu znaku
        pinned = [
            _UPPER[raw[0] % len(_UPPER)],
            _LOWER[raw[1] % len(_LOWER)],
            _DIGITS[raw[2] % len(_DIGITS)],
            _SPECIAL[raw[3] % len(_SPECIAL)] if uses_special else charset[raw[3] % len(charset)],
        ]

        rest = [charset[raw[i + 4] % len(charset)] for i in range(length - 4)]
        chars = pinned + rest

        # Deterministické přemíchání (Fisher-Yates nad hashem)
        for i in range(len(chars) - 1, 0, -1):
            j = raw[i % len(raw)] % (i + 1)
            chars[i], chars[j] = chars[j], chars[i]

        return "".join(chars)

    # ========================================================================
    # Hlavní metoda
    # ========================================================================

    def generate(self, platform: str, phrase: str, extra: str) -> list[str]:
        if not platform.strip() or not phrase.strip() or not extra.strip():
            return []

        return [
            self._derive(platform, phrase, extra, idx, length, charset)
            for idx, (length, charset) in enumerate(_VARIANTS)
        ]
