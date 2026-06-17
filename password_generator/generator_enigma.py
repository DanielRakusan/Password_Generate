from password_generator.generator import PasswordGenerator, CHARSET_FULL, _UPPER, _LOWER, _DIGITS, _SPECIAL


class PasswordGeneratorEnigma(PasswordGenerator):
    # ========================================================================
    # Historická kabeláž rotorů Wehrmacht Enigma (I, II, III) a reflektor B
    # Každý seznam = zamíchaná abeceda A-Z zapsaná jako čísla (A=0, B=1 ...)
    # ========================================================================

    ROTOR_I   = [4, 10, 12,  5, 11,  6,  3, 16, 21, 25, 13, 19, 14,
                22, 24,  7, 23, 20, 18, 15,  0,  8,  1, 17,  2,  9]

    ROTOR_II  = [0,  9,  3, 10, 18,  8, 17, 20, 23,  1, 11,  7, 22,
                19, 12,  2, 16,  6, 25, 13, 15, 24,  5, 21, 14,  4]

    ROTOR_III = [1,  3,  5,  7,  9, 11,  2, 15, 17, 19, 23, 21, 25,
                13, 24,  4,  8, 22,  6,  0, 10, 12, 20, 18, 16, 14]

    REFLECTOR = [24, 17, 20,  7, 16, 18, 11,  3, 15, 23, 13,  6, 14,
                10, 12,  8,  4,  1,  5, 25,  2, 22, 21,  9,  0, 19]

    # ========================================================================
    # Průchod rotorem vpřed
    # ========================================================================

    def _rotor_forward(self, idx, rotor, pos):
        # Posuneme vstup o aktuální pozici rotoru, najdeme v tabulce, posuneme zpátky
        return (rotor[(idx + pos) % 26] - pos) % 26

    # ========================================================================
    # Průchod rotorem zpět (inverzně)
    # ========================================================================

    def _rotor_backward(self, idx, rotor, pos):
        # Hledáme v tabulce kde je naše číslo a vrátíme pozici
        target = (idx + pos) % 26
        for i, val in enumerate(rotor):
            if val == target:
                return (i - pos) % 26
        return idx

    # ========================================================================
    # Celý průchod Enigmou — vpřed, reflektor, zpět
    # ========================================================================

    def _enigma_pass(self, idx, r1, r2, r3):
        # Vpřed přes tři rotory
        idx = self._rotor_forward(idx, self.ROTOR_I,   r1)
        idx = self._rotor_forward(idx, self.ROTOR_II,  r2)
        idx = self._rotor_forward(idx, self.ROTOR_III, r3)

        # Odraz přes reflektor
        idx = self.REFLECTOR[idx]

        # Zpět přes tři rotory pozpátku
        idx = self._rotor_backward(idx, self.ROTOR_III, r3)
        idx = self._rotor_backward(idx, self.ROTOR_II,  r2)
        idx = self._rotor_backward(idx, self.ROTOR_I,   r1)

        return idx

    # ========================================================================
    # Generování hesla
    # ========================================================================

    def _derive_password(self, platform, phrase, extra, variant_idx, length, charset):
        raw = self._get_hash_bytes(platform, phrase, extra, variant_idx)

        # Počáteční pozice rotorů odvozeny ze seedu (0-25 jako v historické Enigmě)
        r1 = raw[0] % 26
        r2 = raw[1] % 26
        r3 = raw[2] % 26

        # Zaručíme přítomnost každého typu znaku
        password = [
            _UPPER[raw[0] % len(_UPPER)],
            _LOWER[raw[1] % len(_LOWER)],
            _DIGITS[raw[2] % len(_DIGITS)],
        ]

        if charset == CHARSET_FULL:
            password.append(_SPECIAL[raw[3] % len(_SPECIAL)])

        for i in range(len(password), length):
            # Enigma vrátí posun (0-25) podle aktuálních pozic rotorů
            enigma_shift = self._enigma_pass(raw[i % len(raw)] % 26, r1, r2, r3)

            # Posun použijeme jako dodatečný krok v znakové sadě
            idx = (raw[i % len(raw)] + enigma_shift) % len(charset)
            password.append(charset[idx])

            # Kaskádové otáčení rotorů — pravý každý znak, střední každých 26, levý každých 676
            r3 = (r3 + 1) % 26
            if r3 == 0:
                r2 = (r2 + 1) % 26
            if r2 == 0:
                r1 = (r1 + 1) % 26

        # Deterministické promíchání
        for i in range(len(password) - 1, 0, -1):
            j = raw[i % len(raw)] % (i + 1)
            password[i], password[j] = password[j], password[i]

        return "".join(password)
