import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "CareBridge AI Healthcare Platform"
    DEBUG: bool = True
    
    # Database Configuration
    # Uses local SQLite fallback if DATABASE_URL isn't configured yet
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "postgresql://postgres:postgres@localhost:5432/carebridge"
    )
    
    # Third-Party AI Engine Credentials
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "your_mock_groq_key_here")

    class Config:
        env_file = ".env"

settings = Settings()
