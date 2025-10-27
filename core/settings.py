import os
import logging
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from exceptions.exceptions import NotFoundException

env_file = ".env"

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
        env_file=env_file,
        extra="allow",
        env_nested_delimiter="__",
        validate_default=False
    )


logger = logging.getLogger("app."+__name__)



if not os.path.exists(env_file):
    logger.info("Not found env file.")
    raise NotFoundException(message=f"{env_file} does not exist")
else:
    settings = Settings()
    logger.info("Settings load succesfully")




