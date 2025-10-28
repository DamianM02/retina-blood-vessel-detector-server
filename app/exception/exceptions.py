from fastapi import status


class AppException(Exception):
    """Base app exception"""
    def __init__(self, message : str, code: str = "APP_ERROR", status_code : int = status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.code = code
        self.status_code = status_code
        super().__init__(message)

class NotFoundException(AppException):
    def __init__(self, message : str = "Resource not found"):
        super().__init__(message=message, code="NOT_FOUND", status_code=status.HTTP_404_NOT_FOUND)

class ValidationException(AppException):
    def __init__(self, message : str = "Validation error"):
        super().__init__(message=message, code="VALIDATION_ERROR", status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ModelInitializationException(AppException):
    def __init__(self, message : str = "Model initialization error"):
        super().__init__(message=message, code="MODEL_INITIALIZATION_ERROR", status_code=status.HTTP_404_NOT_FOUND)