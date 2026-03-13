from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # App Configuration
    APP_NAME: str = "Portfolio Backend"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    PORT: int = 8080

    # Database Configuration (SQL - replacing MongoDB)
    # Use sqlite:///./portfolio.db for SQLite or postgresql://... for PostgreSQL
    DATABASE_URL: str = "sqlite+aiosqlite:///./portfolio.db"
    
    # For PostgreSQL use: postgresql+asyncpg://user:password@localhost/portfolio_db
    # For MySQL use: mysql+aiomysql://user:password@localhost/portfolio_db
    
    @property
    def ASYNC_DATABASE_URL(self) -> str:
        """Convert DATABASE_URL to async driver format"""
        if self.DATABASE_URL.startswith("postgresql://"):
            return self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)
        elif self.DATABASE_URL.startswith("mysql://"):
            return self.DATABASE_URL.replace("mysql://", "mysql+aiomysql://", 1)
        return self.DATABASE_URL
    
    MONGODB_URI: str = ""  # Deprecated - kept for compatibility
    MONGODB_DATABASE: str = "portfolio_db"  # Deprecated

    # Email Configuration (Resend)
    RESEND_API_KEY: str = ""
    RESEND_FROM_EMAIL: str = "hello@rajshekhar.live"
    
    # Email Constants
    REPLY_TO_EMAIL: str = "rajsingh170901@gmail.com"
    ADMIN_EMAIL: str = "rajsingh170901@gmail.com"

    # CORS
    CORS_ORIGIN: str = "https://raj-shekhar-portfolio.netlify.app"

    @property
    def CORS_ORIGINS(self) -> list:
        return [origin.strip() for origin in self.CORS_ORIGIN.split(",")]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

