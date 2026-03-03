from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # App Configuration
    APP_NAME: str = "Portfolio Backend"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    PORT: int = 8080

    # MongoDB Configuration
    MONGODB_URI: str = "mongodb://localhost:27017"
    MONGODB_DATABASE: str = "portfolio_db"

    # Email Configuration (Resend)
    RESEND_API_KEY: str = ""
    RESEND_FROM_EMAIL: str = "hello@rajshekhar.live"
    
    # Email Constants
    REPLY_TO_EMAIL: str = "rajsingh170901@gmail.com"
    ADMIN_EMAIL: str = "rajsingh170901@gmail.com"

    # CORS
    CORS_ORIGIN: str = "https://raj-shekhar-portfolio.netlify.app"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

