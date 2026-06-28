import random


class RandomData:
    """
    Generates random test data.
    """

    @staticmethod
    def generate_email():
        number = random.randint(100000, 999999)
        return f"qatest{number}@gmail.com"