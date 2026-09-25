import uuid


class RandomData:
    """
    Generates random test data.
    """

    @staticmethod
    def generate_email():
        # example.com is reserved for testing, so no real inbox is ever used
        return f"qa.demo.{uuid.uuid4().hex[:10]}@example.com"
