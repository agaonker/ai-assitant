from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "AI Personal Assistant"
    
    # Model Configuration
    MODEL_NAME: str = "gpt2"  # Default model, can be changed to other open-source models
    MAX_TOKENS: int = 1000
    TEMPERATURE: float = 0.7
    
    # Server Configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    class Config:
        case_sensitive = True

settings = Settings() 