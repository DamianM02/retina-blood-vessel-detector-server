import os
import sys
import logging
from pythonjsonlogger import jsonlogger
from dotenv import load_dotenv

def setup_logger():
    load_dotenv()

    level = logging.DEBUG if os.environ.get("DEBUG") else logging.WARNING
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        jsonlogger.JsonFormatter(
            "%(asctime)s %(levelname)s %(name)s %(message)s]",
            style="%"
        )
    )
    root_logger.addHandler(handler)

    for uvicorn_logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        uvicorn_logger = logging.getLogger(uvicorn_logger_name)
        uvicorn_logger.handlers.clear()
        uvicorn_logger.propagate= True
        uvicorn_logger.setLevel(logging.NOTSET) # Due to this, level will be root level
