import hashlib


_UPPER   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_LOWER   = "abcdefghijklmnopqrstuvwxyz"
_DIGITS  = "0123456789"
_SPECIAL = "!@#$%&*?"

CHARSET_FULL  = _UPPER + _LOWER + _DIGITS + _SPECIAL
CHARSET_ALNUM = _UPPER + _LOWER + _DIGITS
CHARSET_SAFE  = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz23456789"


class PasswordGenerator:
    # ========================================================================
    # Varianty hesel (délka, charset)
    # ========================================================================

    VARIANTS = [
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

    # ========================================================================
    # Derivace jednoho hesla
    # ========================================================================

    def _get_hash_bytes(self, platform, phrase, extra, variant_idx):
        # Kombinujeme vstupy a index varianty — každý index dá jiné heslo
        seed = f"{platform}|{phrase}|{extra}|{variant_idx}".encode("utf-8")

        raw = b""
        current = seed
        while len(raw) < 64:
            current = hashlib.sha256(current).digest()
            raw += current

        return raw

    def _derive_password(self, platform, phrase, extra, variant_idx, length, charset):
        raw = self._get_hash_bytes(platform, phrase, extra, variant_idx)

        # Zaručíme přítomnost každého typu znaku
        password = [
            _UPPER[raw[0] % len(_UPPER)],
            _LOWER[raw[1] % len(_LOWER)],
            _DIGITS[raw[2] % len(_DIGITS)],
        ]

        if charset == CHARSET_FULL:
            password.append(_SPECIAL[raw[3] % len(_SPECIAL)])

        for i in range(len(password), length):
            password.append(charset[raw[i] % len(charset)])

        # Deterministické promíchání — Fisher-Yates nad hashem
        for i in range(len(password) - 1, 0, -1):
            j = raw[i % len(raw)] % (i + 1)
            password[i], password[j] = password[j], password[i]

        return "".join(password)

    # ========================================================================
    # Hlavní metoda
    # ========================================================================

    def generate(self, platform, phrase, extra):
        if not platform.strip() or not phrase.strip() or not extra.strip():
            return []

        passwords = []
        for idx, (length, charset) in enumerate(self.VARIANTS):
            pwd = self._derive_password(platform, phrase, extra, idx, length, charset)
            passwords.append(pwd)

        return passwords
