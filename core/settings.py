import os
import logging
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from exceptions.exceptions import NotFoundException

logger = logging.getLogger("app."+__name__)


class Middleware(BaseModel):
    allow_origins : list[str]
    allow_credentials : bool
    allow_methods: list[str]
    allow_headers: list[str]


class Settings(BaseSettings):
    unet_size : int = 512
    state_dict_path : str
    middleware: Middleware
    debug : bool = False
    only_app_debug : bool = True
    logger_file : str = None
    console_debug : bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow",
        env_nested_delimiter="__",
        validate_default=False
    )



settings : Settings | None = None

def get_settings() -> Settings: # Lepiej zrobić taki getter czy zostawić tak jak w kazdej innej czesci projektu, czyli zwykły import zmiennej settings?
    if settings:
        return settings
    else:
        logger.warning("Settings are not initialized.")
        raise NotFoundException()


def init_settings():
    if not os.path.exists(".env"):
        logger.info("Not found env file.")
    else:
        global settings # Czy tak mogę?
        settings = Settings()
        logger.info("Settings load succesfully.")




