from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from exceptions.exceptions import NotFoundException
from repositories.model_repository import ModelRepository

logger = logging.getLogger("app."+__name__)




model_repo : ModelRepository | None = None

def get_model_repo() -> ModelRepository:
    if model_repo:
        return model_repo
    else:
        logger.warning("Model repository is not initialized.")
        raise NotFoundException()



@asynccontextmanager
async def lifespan(app: FastAPI, state_dict_path):
    logger.info("Server starting...")
    global model_repo # Czy tak mogę?
    model_repo = ModelRepository()
    model_repo.load_state_dict_from_path(state_dict_path)
    logger.info("Server started succesfully.")
    yield
    logger.info("Server closing...")

