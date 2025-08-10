from pathlib import Path
from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


class CustomBaseSettings(BaseSettings):
    """Global base settings model allowing to customize all models within the app."""

    ENV_FILENAME: ClassVar[str] = ".env"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parents[3] / ENV_FILENAME,
    )


class Settings(CustomBaseSettings):
    """Global settings class."""

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "vectorstore"
    POSTGRES_SCHEMA: str = "public"
    POSTGRES_SYNC_PREFIX: str = "postgresql+psycopg"
    POSTGRES_ASYNC_PREFIX: str = "postgresql+asyncpg"

    VECTOR_DIMS: int = 768

    def get_database_url(self, is_async: bool = False) -> str:
        prefix = self.POSTGRES_ASYNC_PREFIX if is_async else self.POSTGRES_SYNC_PREFIX
        return f"{prefix}://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings = Settings()
