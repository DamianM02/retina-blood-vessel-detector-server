from other.swagger_dark_theme import DarkThemeRouter
import json

# settings_json = json.load(open("settings.json", "rb"))  # TODO: error handling with settings

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from exceptions import exception_handlers

from models.SegmentationUNET import model
# TODO: error hangling with model

model = None
settings_json = None



app = FastAPI(docs_url=None)  # must be docs_url = None, cause im using fastapi stagger dark
# Dark Theme for Swagger
DarkThemeRouter(app).make_dark_theme()



app.add_exception_handler(FileNotFoundError, exception_handlers.file_not_found_handler)



app.add_middleware(
    CORSMiddleware,
    allow_origns=settings_json["middleware"]["allow_origins"],
    allow_credentials=settings_json["middleware"]["allow_credentials"],
    allow_methods=settings_json["middleware"]["allow_methods"],
    allow_headers=settings_json["middleware"]["allow_headers"]
)


