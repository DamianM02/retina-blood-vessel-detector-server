from contextlib import asynccontextmanager
from fastapi import FastAPI

from repositories.model_repository import ModelRepository


model_repo = ModelRepository()

def get_model_repo() -> ModelRepository:
    return model_repo


@asynccontextmanager
async def lifespan(app: FastAPI, state_dict_path):
    model_repo.load_state_dict_from_path(state_dict_path)
    print("Server started succesfully.")
    yield
    print("Server is closing...")
