from password_generator.generator import PasswordGenerator


class PasswordGeneratorSHA1(PasswordGenerator):
    ALGORITHM = "sha1"
