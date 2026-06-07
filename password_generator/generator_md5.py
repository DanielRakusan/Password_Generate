from password_generator.generator import PasswordGenerator


class PasswordGeneratorMD5(PasswordGenerator):
    ALGORITHM = "md5"
