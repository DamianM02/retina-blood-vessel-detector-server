

from core.logger import setup_logger

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from core.lifespan import lifespan
from other.swagger_dark_theme import DarkThemeRouter

from controllers import inference_controller

from core.settings import init_settings, get_settings
from exceptions.exception_handlers import register_exception_handlers



from repositories.settings_json_repository import SettingsJSONRepository
# I decided to only one time load json with settings
# settings_json_repo = SettingsJSONRepository()
# settings_json_repo.load("settings.json")

setup_logger()
init_settings()
settings = get_settings()


app = FastAPI(docs_url=None, # must be docs_url = None, cause im using fastapi stagger dark theme
              lifespan=lambda app: lifespan(app, settings.state_dict_path)
              )

# Dark Theme for Swagger
DarkThemeRouter(app).make_dark_theme()


register_exception_handlers(app)

app.include_router(inference_controller.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.middleware.allow_origins,
    allow_credentials=settings.middleware.allow_credentials,
    allow_methods=settings.middleware.allow_methods,
    allow_headers=settings.middleware.allow_headers
)

