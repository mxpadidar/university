from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class __Configs__(BaseSettings):
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    DEBUG: bool = True
    SECRET_KEY: str = "secret"

    POSTGRES_DRIVER: str = "postgresql+psycopg"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5433
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "postgres"

    MINIO_HOST: str = "localhost"
    MINIO_PORT: int = 9000
    MINIO_ACCESS_KEY: str = "minio"
    MINIO_SECRET_KEY: str = "minio123"

    @property
    def POSTGRES_URI(self):
        return f"{self.POSTGRES_DRIVER}://\
            {self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/\
            {self.POSTGRES_DB}".replace(" ", "")  # fmt: skip

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
    )


configs = __Configs__()
