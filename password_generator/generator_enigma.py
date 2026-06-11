from password_generator.generator import PasswordGenerator, CHARSET_FULL, _UPPER, _LOWER, _DIGITS, _SPECIAL


class PasswordGeneratorEnigma(PasswordGenerator):
    # ========================================================================
    # Enigma — tři rotory s postupným posunem jako u historické šifrovací stroje
    # ========================================================================

    def _derive_password(self, platform, phrase, extra, variant_idx, length, charset):
        raw = self._get_hash_bytes(platform, phrase, extra, variant_idx)

        # Tři rotory — počáteční pozice odvozeny ze seedu
        rotor1 = raw[0] % len(charset)
        rotor2 = raw[1] % len(charset)
        rotor3 = raw[2] % len(charset)

        # Zaručíme přítomnost každého typu znaku
        password = [
            _UPPER[raw[0] % len(_UPPER)],
            _LOWER[raw[1] % len(_LOWER)],
            _DIGITS[raw[2] % len(_DIGITS)],
        ]

        if charset == CHARSET_FULL:
            password.append(_SPECIAL[raw[3] % len(_SPECIAL)])

        for i in range(len(password), length):
            # Kombinovaný posun ze všech tří rotorů
            shift = (rotor1 + rotor2 + rotor3) % len(charset)
            idx = (raw[i % len(raw)] + shift) % len(charset)
            password.append(charset[idx])

            # Rotory se posouvají jako v Enigmě — druhý až po přetečení prvního
            rotor1 = (rotor1 + 1) % len(charset)
            if rotor1 == 0:
                rotor2 = (rotor2 + 1) % len(charset)
            if rotor2 == 0:
                rotor3 = (rotor3 + 1) % len(charset)

        # Deterministické promíchání
        for i in range(len(password) - 1, 0, -1):
            j = raw[i % len(raw)] % (i + 1)
            password[i], password[j] = password[j], password[i]

        return "".join(password)
