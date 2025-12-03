from dataclasses import dataclass
import os


@dataclass
class Settings:
    base_url: str
    timeout: float = 5.0


def get_settings() -> Settings:
    """
    Get framework config from environment variables
    (or default values).
    """
    return Settings(
        base_url=os.getenv("API_BASE_URL", "https://postman-echo.com"),
        timeout=float(os.getenv("API_TIMEOUT", "5.0")),
    )