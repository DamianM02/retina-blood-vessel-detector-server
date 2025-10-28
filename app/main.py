

from app.core.logger import setup_logger

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.core.lifespan import lifespan
from app.other.swagger_dark_theme import DarkThemeRouter

from app.controller import inference_controller

from app.core.settings import Settings, init_settings
from app.exception.exception_handlers import register_exception_handlers


setup_logger()

init_settings() # Wsm do zastanowienia się czy nie można tego zrobić lepiej

settings = Settings()




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

