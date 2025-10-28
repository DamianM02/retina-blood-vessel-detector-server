from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from app.exception.exceptions import NotFoundException
from app.repository.model_repository import ModelRepository

logger = logging.getLogger("app."+__name__)



@asynccontextmanager
async def lifespan(app: FastAPI, state_dict_path):
    logger.info("Server starting...")
    global model_repo # Czy tak mogę?
    model_repo = ModelRepository()
    model_repo.load_state_dict_from_path(state_dict_path)
    logger.info("Server started succesfully.")
    yield
    logger.info("Server closing...")

