from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or .env file.
    """

    # Application settings
    APP_NAME: str = "ContextFlow"
    ENVIRONMENT: str = "development"  # E.g., development, staging, production
    SECRET_KEY: str = "default_secret_key_change_me"  # MUST be overridden in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database settings
    DATABASE_URL: str = (
        "postgresql+asyncpg://user:password@localhost:5432/contextflow_db"
    )

    # RabbitMQ settings
    RABBITMQ_URL: str = "amqp://guest:guest@localhost:5672/"

    # Define model config to load from .env file
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


# Cache the settings object to avoid reloading it multiple times
@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
