import json
import os

class Storage:
    def __init__(self, filename: str):
        self.filename = filename

    def load_data(self):
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            print(" Fel vid läsning av databasfil, skapar en ny.")
            return {}

    def save_data(self, data):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f" Kunde inte spara data: {e}")
