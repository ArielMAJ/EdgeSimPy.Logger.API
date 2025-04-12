from fastapi import Header

from src.config.env import Config
from src.exceptions.http_exceptions import CredentialsException


def api_key_dependency(api_key: str | None = Header(None, alias="API-KEY")):
    """
    Dependency to validate the API-KEY header.
    """
    if not api_key or api_key != Config.API_KEY:
        raise CredentialsException()
