import uuid
from typing import Any

from pgvector.sqlalchemy import Vector
from sqlalchemy import Text, text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .settings import settings


class CustomBaseModel(DeclarativeBase):
    """Custom base database model class."""

    __table_args__ = {"schema": settings.POSTGRES_SCHEMA}


class VectorStore(CustomBaseModel):
    """Database model class for embeddings."""

    __tablename__ = "vectorstore"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
        server_default=text("uuid_generate_v4()"),
    )
    content: Mapped[str] = mapped_column(Text(), unique=True)
    embedding: Mapped[list[float]] = mapped_column(Vector(dim=settings.VECTOR_DIMS))
    meta: Mapped[dict[str, Any]] = mapped_column(JSONB, name="metadata")
