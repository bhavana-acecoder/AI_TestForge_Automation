import logging
import os


class Logger:

    @staticmethod
    def get_logger():

        if not os.path.exists("logs"):
            os.makedirs("logs")

        logger = logging.getLogger("QAFramework")

        if logger.hasHandlers():
            return logger

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler("logs/framework.log")

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger