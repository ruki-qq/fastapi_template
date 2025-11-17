from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "db_dev"
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 5432
    api_prefix: str = "/api/v1"

    echo: bool = True

    @property
    def url(self) -> str:
        return (
            "postgresql+asyncpg://"
            f"{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


class Settings:
    db: DBSettings = DBSettings()


settings = Settings()
