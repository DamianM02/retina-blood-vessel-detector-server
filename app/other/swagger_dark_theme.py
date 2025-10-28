from fastapi import APIRouter, FastAPI
import fastapi_swagger_dark as fsd


class DarkThemeRouter:
    def __init__(self, app: FastAPI):
        self.app = app

    def make_dark_theme(self):
        router = APIRouter()
        fsd.install(router)
        self.app.include_router(router)
