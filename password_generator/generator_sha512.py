from password_generator.generator import PasswordGenerator


class PasswordGeneratorSHA512(PasswordGenerator):
    ALGORITHM = "sha512"
