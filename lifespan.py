from contextlib import asynccontextmanager
from fastapi import FastAPI
from
import json
import os

@asynccontextmanager
async def lifespan(app:FastAPI):
    global model
    global setting_json

    json_path = os.path.join("./", "setting.json")
    setting_json = json.load(open(json_path, "rb"))

    model =
