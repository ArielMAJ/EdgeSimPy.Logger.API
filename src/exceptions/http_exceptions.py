from fastapi import HTTPException, status

from src.database.models.model_base import ModelBase


class NotFoundException(HTTPException):
    def __init__(self, model: ModelBase):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{model.__name__} not found",
        )


class CredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized: Invalid or missing API-KEY",
        )
