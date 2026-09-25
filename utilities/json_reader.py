import json
from pathlib import Path

# Project root folder (one level above utilities/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent


class JsonReader:

    @staticmethod
    def read_json(file_path):
        """
        Read a JSON file. The path is relative to the project root,
        for example "testdata/register.json", so tests work from any folder.
        """
        with open(PROJECT_ROOT / file_path, "r", encoding="utf-8") as file:
            return json.load(file)
