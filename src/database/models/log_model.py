from sqlalchemy import JSON, UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.model_base import ModelBase


class LogModel(ModelBase):
    __tablename__ = "logs"

    hash: Mapped[UUID] = mapped_column(UUID(), nullable=False, unique=False, index=True)

    input_simulation: Mapped[dict] = mapped_column(
        JSON(), nullable=False, unique=False, index=False
    )
    agent_metrics: Mapped[dict] = mapped_column(
        JSON(), nullable=False, unique=False, index=False
    )
    algorithm: Mapped[str] = mapped_column(
        String(50), nullable=False, unique=False, index=False
    )
