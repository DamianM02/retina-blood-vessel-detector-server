import json


class SettingsJSONRepository:
    def __init__(self):
        self._settings = None

    @property
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, settings: dict):
        self._settings = settings

    def load(self, path:str):
        self.settings = json.load(open(path, "rb"))