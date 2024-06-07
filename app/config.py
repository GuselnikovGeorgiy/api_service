from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    APP_HOST: str
    APP_PORT: int
    MONGO_DB_ADMIN_USERNAME: str
    MONGO_DB_ADMIN_PASSWORD: str

    @property
    def DATABASE_URL(self) -> str:
        return f"mongodb://{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
