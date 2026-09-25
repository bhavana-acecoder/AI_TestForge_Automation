import logging
import os

class APILogger:
    @staticmethod
    def get_logger():
        # Ensure a 'logs' directory exists
        os.makedirs("logs", exist_ok=True)

        # Create a logger object
        logger = logging.getLogger("API Logger")
        logger.setLevel(logging.INFO)

        # Avoid adding multiple handlers if already added
        if not logger.handlers:
            file_handler = logging.FileHandler("logs/api.log")
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger