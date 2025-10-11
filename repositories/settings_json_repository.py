import json
import logging

logger = logging.getLogger("app."+ __name__)


class SettingsJSONRepository:
    def __init__(self):
        logger.info("Initializing SettingJSONRepository...")
        self._settings = None

    @property
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, settings: dict):
        self._settings = settings

    def load(self, path:str):
        logger.info("Loading SettingJSON...")
        self.settings = json.load(open(path, "rb"))