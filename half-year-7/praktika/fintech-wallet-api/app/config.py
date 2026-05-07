from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FinTech Wallet API"
    secret_key: str = "change_me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    database_url: str = "sqlite:///./fintech.db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
