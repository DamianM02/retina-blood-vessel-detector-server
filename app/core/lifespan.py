from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging
from app.core.settings import init_settings

from app.repository.model_repository import ModelRepository

logger = logging.getLogger("app." + __name__)


@asynccontextmanager
async def lifespan(app: FastAPI, state_dict_path):
    logger.info("Server starting...")
    init_settings()
    model_repo = ModelRepository()
    model_repo.load_state_dict_from_path(state_dict_path)
    logger.info("Server started succesfully.")
    yield
    logger.info("Server closing...")
