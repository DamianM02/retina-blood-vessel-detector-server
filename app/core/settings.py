import os
import logging
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from app.utils.singleton import singleton

logger = logging.getLogger("app."+__name__)

@singleton
class Settings(BaseSettings):
    class MiddlewareWrapper(BaseModel):
        allow_origins: list[str]
        allow_credentials: bool
        allow_methods: list[str]
        allow_headers: list[str]

    unet_size: int = 512
    state_dict_path: str
    middleware: MiddlewareWrapper
    debug: bool = False
    only_app_debug: bool = True
    logger_file: str = None
    console_debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow",
        env_nested_delimiter="__",
        validate_default=False
    )

def init_settings():
    if not os.path.exists(".env"):
        logger.warning("Not found .env file.")
    else:
        Settings()
        logger.info("Settings load succesfully.")

