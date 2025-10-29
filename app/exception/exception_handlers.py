import logging

from fastapi import Request
from fastapi.responses import JSONResponse
import fastapi
from fastapi import status

from app.exception.exceptions import AppException

logger = logging.getLogger("app." + __name__)


async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    logger.warning(f"AppException: {exc.code} - {exc.message} - {request.url.path}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.code, "details": exc.message, "path": request.url.path},
    )


async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.warning(f"UnhandledException: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "details": str(exc),
            "path": request.url.path,
        },
    )


def register_exception_handlers(app: fastapi.applications.FastAPI):
    app.add_exception_handler(AppException, app_exception_handler)
    app.add_exception_handler(Exception, generic_exception_handler)
