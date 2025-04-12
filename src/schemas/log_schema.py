from uuid import UUID

from pydantic import BaseModel


class LogSchema(BaseModel):
    hash: UUID
    input_simulation: dict
    agent_metrics: dict
    algorithm: str
