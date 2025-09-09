from fastapi import Request
from fastapi.responses import JSONResponse


def file_not_found_handler(request: Request, exc: FileNotFoundError) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"error": "file not exist", "message": str(exc)}
    )
