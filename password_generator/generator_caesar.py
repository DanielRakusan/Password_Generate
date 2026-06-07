from password_generator.generator import PasswordGenerator, CHARSET_FULL, _UPPER, _LOWER, _DIGITS, _SPECIAL


class PasswordGeneratorCaesar(PasswordGenerator):
    # ========================================================================
    # Caesarova šifra — rotace výstupní abecedy
    # ========================================================================

    def _derive_password(self, platform, phrase, extra, variant_idx, length, charset):
        raw = self._get_hash_bytes(platform, phrase, extra, variant_idx)

        # Caesarův posun: sečteme ASCII hodnoty všech vstupů
        seed_str = f"{platform}{phrase}{extra}"
        shift = sum(ord(c) for c in seed_str) % len(charset)

        # Rotujeme charset o shift pozic — to je podstata Caesarovy šifry
        caesar_charset = charset[shift:] + charset[:shift]

        # Zaručíme přítomnost každého typu znaku
        password = [
            _UPPER[raw[0] % len(_UPPER)],
            _LOWER[raw[1] % len(_LOWER)],
            _DIGITS[raw[2] % len(_DIGITS)],
        ]

        if charset == CHARSET_FULL:
            password.append(_SPECIAL[raw[3] % len(_SPECIAL)])

        for i in range(len(password), length):
            password.append(caesar_charset[raw[i] % len(caesar_charset)])

        # Deterministické promíchání
        for i in range(len(password) - 1, 0, -1):
            j = raw[i % len(raw)] % (i + 1)
            password[i], password[j] = password[j], password[i]

        return "".join(password)
