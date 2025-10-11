from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from repositories.model_repository import ModelRepository

logger = logging.getLogger("app."+__name__)

def f():
    print("xd")
    logger.info("siema")
    print("xd2")


model_repo = ModelRepository()

def get_model_repo() -> ModelRepository:
    return model_repo



@asynccontextmanager
async def lifespan(app: FastAPI, state_dict_path):
    logger.info("Server starting...")
    model_repo.load_state_dict_from_path(state_dict_path)
    logger.info("Server started succesfully.")
    yield
    logger.info("Server closing...")

