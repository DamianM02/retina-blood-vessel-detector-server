import sys
import logging
from pythonjsonlogger import jsonlogger
from core.settings import settings


# from logging.config import dictConfig
# level = "DEBUG" if settings.debug else "WARNING"
#
# LOGGING_CONFIG = {
#     "version": 1,
#     "disable_existing_loggers": False,  # ważne, żeby nie wyłączyć uvicornowych
#     "formatters": {
#         "default": {
#             "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
#         },
#     },
#     "handlers": {
#         "default": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             "formatter": "default",
#         },
#     },
#     "loggers": {
#         "uvicorn.error": {"handlers": ["default"], "level": "INFO"},
#         "uvicorn.access": {"handlers": ["default"], "level": "INFO"},
#         "app": {"handlers": ["default"], "level": "DEBUG", "propagate": False},
#     },
#     "root": {
#         "level": level,
#         "handlers": ["default"],
#     },
# }
#
# dictConfig(LOGGING_CONFIG)





# print(f"My level {level}")



# root_logger = logging.getLogger()
# print(f"Root previous level {root_logger.level}")
#
# example_logger = logging.getLogger("example")
# print(f"Example previous level {example_logger.level}")
#
# root_logger.setLevel(level)
# print(f"Root present level {root_logger.level}")
# print(f"Example present level {example_logger.level}")
#
# example2_logger = logging.getLogger("example2")
# print(f"Example2 present level {example2_logger.level}")
#
# # example_logger.setLevel(logging.DEBUG)
# print(f"Example future level {example_logger.level}")


level = logging.DEBUG if settings.debug else logging.WARNING
root_logger = logging.getLogger()
root_logger.setLevel(level)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(
    jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s]",
        style="%"
    )
)
# handler.setLevel(level) #unnecessary
root_logger.addHandler(handler)

for uvicorn_logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
    uvicorn_logger = logging.getLogger(uvicorn_logger_name)
    uvicorn_logger.handlers.clear()
    uvicorn_logger.propagate= True
    uvicorn_logger.setLevel(logging.NOTSET) # Due to this, level will be root level



# if settings.logger_file and settings.logger_file != "":
#     file_handler = logging.handlers.RotatingFileHandler(settings.logger_file, maxBytes=1_000_000, backupCount=3)
#     file_handler.setFormatter(jsonlogger.JsonFormatter(
#         fmt = "asctime levelname name message"
#     ))
#     # file_handler.setLevel(level) #unnecessary
#     root_logger.addHandler(file_handler)

# if settings.console_debug:
#     console_handler = logging.StreamHandler()
#     console_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s,,, %(tags)s"))
#     # console_handler.setLevel(level) #unnecessary
#     root_logger.addHandler(console_handler)
#











