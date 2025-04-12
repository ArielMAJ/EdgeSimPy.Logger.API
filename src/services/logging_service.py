from loguru import logger

from src.database.models.log_model import LogModel
from src.exceptions.http_exceptions import NotFoundException
from src.schemas.log_schema import LogSchema


class LoggingService:
    async def get_log(self, hash: str) -> LogSchema:
        """
        Retrieve a log by hash.

        Args:
            hash (str): The randomly generated UUID hash for the log.

        Returns:
            Log: The EdgeSimPy simulation Log object.
        """
        logger.info(f"Retrieving log with hash {hash} from database")
        log: LogModel | None = await LogModel.get(hash=hash)
        if log is None:
            raise NotFoundException(LogModel)

        return LogSchema(
            hash=log.hash,
            input_simulation=log.input_simulation,
            agent_metrics=log.agent_metrics,
            algorithm=log.algorithm,
        )

    async def create_log(self, log: LogSchema) -> None:
        """
        Create a new log.

        Args:
            log (Log): The log data.

        Returns:
            None
        """
        logger.info(f"Saving log with hash {log.hash} to database")
        await LogModel.new(**log.model_dump())
