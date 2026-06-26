"""
AEGIS AI Settings

All application configuration is managed from this file.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # -------------------------------------------------
    # Application
    # -------------------------------------------------
    APP_NAME: str = "AEGIS AI"
    APP_VERSION: str = "0.0.2"
    APP_DESCRIPTION: str = "Institutional AI Trading Platform"

    # -------------------------------------------------
    # General
    # -------------------------------------------------
    DEBUG: bool = True
    TIMEZONE: str = "Asia/Kolkata"

    # -------------------------------------------------
    # Trading
    # -------------------------------------------------
    DEFAULT_SYMBOL: str = "XAUUSD"

    # -------------------------------------------------
    # Environment
    # -------------------------------------------------
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()