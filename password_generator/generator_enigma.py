import hashlib

from password_generator.generator import PasswordGenerator, CHARSET_FULL, _UPPER, _LOWER, _DIGITS, _SPECIAL


class PasswordGeneratorEnigma(PasswordGenerator):
    enigma_key = None

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
    # Generování vlastní kabeláže rotoru z klíče (Fisher-Yates shuffle)
    # ========================================================================

    def _make_rotor(self, key_bytes, offset):
        rotor = list(range(26))
        for i in range(25, 0, -1):
            j = key_bytes[(offset + i) % len(key_bytes)] % (i + 1)
            rotor[i], rotor[j] = rotor[j], rotor[i]
        return rotor

    def _make_reflector(self, key_bytes):
        # Reflektor musí být involuční permutace (p[p[i]] == i, p[i] != i)
        indices = list(range(26))
        reflector = [0] * 26
        i = 0
        while len(indices) >= 2:
            j = 1 + (key_bytes[(78 + i) % len(key_bytes)] % (len(indices) - 1))
            a = indices.pop(0)
            b = indices.pop(j - 1)
            reflector[a] = b
            reflector[b] = a
            i += 1
        return reflector

    # ========================================================================
    # Sestavení tabulek rotorů — historické nebo z vlastního klíče
    # ========================================================================

    def build_rotors(self, key=None):
        if key is None:
            return self.ROTOR_I, self.ROTOR_II, self.ROTOR_III, self.REFLECTOR
        key_bytes = hashlib.sha256(key.encode("utf-8")).digest()
        return (
            self._make_rotor(key_bytes, 0),
            self._make_rotor(key_bytes, 26),
            self._make_rotor(key_bytes, 52),
            self._make_reflector(key_bytes),
        )

    # ========================================================================
    # Průchod rotorem vpřed
    # ========================================================================

    def _rotor_forward(self, idx, rotor, pos):
        return (rotor[(idx + pos) % 26] - pos) % 26

    # ========================================================================
    # Průchod rotorem zpět (inverzně)
    # ========================================================================

    def _rotor_backward(self, idx, rotor, pos):
        target = (idx + pos) % 26
        for i, val in enumerate(rotor):
            if val == target:
                return (i - pos) % 26
        return idx

    # ========================================================================
    # Celý průchod Enigmou — vpřed, reflektor, zpět
    # ========================================================================

    def _enigma_pass(self, idx, r1, r2, r3, rotor_i, rotor_ii, rotor_iii, reflector):
        idx = self._rotor_forward(idx, rotor_i,   r1)
        idx = self._rotor_forward(idx, rotor_ii,  r2)
        idx = self._rotor_forward(idx, rotor_iii, r3)
        idx = reflector[idx]
        idx = self._rotor_backward(idx, rotor_iii, r3)
        idx = self._rotor_backward(idx, rotor_ii,  r2)
        idx = self._rotor_backward(idx, rotor_i,   r1)
        return idx

    # ========================================================================
    # Generování hesla
    # ========================================================================

    def _derive_password(self, platform, phrase, extra, variant_idx, length, charset):
        raw = self._get_hash_bytes(platform, phrase, extra, variant_idx)

        # Počáteční pozice rotorů odvozeny ze seedu
        r1 = raw[0] % 26
        r2 = raw[1] % 26
        r3 = raw[2] % 26

        # Bez klíče = historické tabulky Wehrmacht, s klíčem = vlastní tabulky
        if self.enigma_key:
            key_bytes = hashlib.sha256(self.enigma_key.encode("utf-8")).digest()
            rotor_i   = self._make_rotor(key_bytes, 0)
            rotor_ii  = self._make_rotor(key_bytes, 26)
            rotor_iii = self._make_rotor(key_bytes, 52)
            reflector = self._make_reflector(key_bytes)
        else:
            rotor_i   = self.ROTOR_I
            rotor_ii  = self.ROTOR_II
            rotor_iii = self.ROTOR_III
            reflector = self.REFLECTOR

        # Zaručíme přítomnost každého typu znaku
        password = [
            _UPPER[raw[0] % len(_UPPER)],
            _LOWER[raw[1] % len(_LOWER)],
            _DIGITS[raw[2] % len(_DIGITS)],
        ]

        if charset == CHARSET_FULL:
            password.append(_SPECIAL[raw[3] % len(_SPECIAL)])

        for i in range(len(password), length):
            enigma_shift = self._enigma_pass(
                raw[i % len(raw)] % 26, r1, r2, r3,
                rotor_i, rotor_ii, rotor_iii, reflector
            )
            idx = (raw[i % len(raw)] + enigma_shift) % len(charset)
            password.append(charset[idx])

            r3 = (r3 + 1) % 26
            if r3 == 0:
                r2 = (r2 + 1) % 26
            if r2 == 0:
                r1 = (r1 + 1) % 26

        for i in range(len(password) - 1, 0, -1):
            j = raw[i % len(raw)] % (i + 1)
            password[i], password[j] = password[j], password[i]

        return "".join(password)
