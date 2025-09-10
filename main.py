from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from exceptions import exception_handlers

from core.lifespan import lifespan
from other.swagger_dark_theme import DarkThemeRouter
from repositories.settings_json_repository import SettingsJSONRepository
from controllers import inference_controller

# I decided to only one time load json with settings
settings_json_repo = SettingsJSONRepository()
settings_json_repo.load("settings.json")





app = FastAPI(docs_url=None, # must be docs_url = None, cause im using fastapi stagger dark
              lifespan=lambda app: lifespan(app, settings_json_repo.settings["state_dict_path"])
              )
# Dark Theme for Swagger
DarkThemeRouter(app).make_dark_theme()


app.add_exception_handler(FileNotFoundError, exception_handlers.file_not_found_handler)
app.include_router(inference_controller.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings_json_repo.settings["middleware"]["allow_origins"],
    allow_credentials=settings_json_repo.settings["middleware"]["allow_credentials"],
    allow_methods=settings_json_repo.settings["middleware"]["allow_methods"],
    allow_headers=settings_json_repo.settings["middleware"]["allow_headers"]
)
