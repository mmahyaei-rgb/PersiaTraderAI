import json


class Settings:

    def __init__(self):

        with open("settings.json", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def database(self):
        return self.data["database"]

    @property
    def log_level(self):
        return self.data["log_level"]

    @property
    def update_interval(self):
        return self.data["update_interval"]

    @property
    def max_symbols(self):
        return self.data["max_symbols"]
    