from fastapi import APIRouter

from src.schemas.log_schema import LogSchema
from src.services.logging_service import LoggingService

router = APIRouter()


@router.get("/{hash}", response_model=LogSchema, status_code=200)
async def get_full_log_by_hash(hash: str) -> LogSchema:
    """
    Retrieve full log by hash.

    Args:
        hash (str): The randomly generated UUID hash for the log.

    Returns:
        Log: The EdgeSimPy simulation LogSchema object.
    """
    return await LoggingService().get_log(hash)


@router.get("/{hash}/metrics", response_model=dict, status_code=200)
async def get_log_metrics_by_hash(hash: str) -> dict:
    """
    Retrieve log metrics by hash.

    Args:
        hash (str): The randomly generated UUID hash for the log.

    Returns:
        Log: The EdgeSimPy simulation LogSchema object.
    """
    return (await LoggingService().get_log(hash)).agent_metrics


@router.post("/", response_model=None, status_code=201)
async def save_log(log: LogSchema) -> None:
    """
    Saves a log item.

    Args:
        log (LogSchema): The log data.

    Returns:
        None
    """
    await LoggingService().create_log(log)
