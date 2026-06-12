from functools import lru_cache
from typing import Literal, List
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config=SettingsConfigDict(
        env_file="../.env.development",
        case_sensitive=False,
        extras="ignore"
    )

    app_name: str="RAG System"
    environment: Literal["development", "staging", "production", "test"]="development"
    log_level: str="INFO"
    secret_key: str
    app_version: str="0.1.0"
    debug: bool=True
    api_v1_prefix:str="/api/v1"
    backend_cors_origins: List[str]=["http://localhost:3000", "http://localhost:8000"]
    access_token_expires_minutes: int=30
    refresh_token_expire_days: int=7

    @property
    def is_development(self)->bool:
        return self.environment=="development"
    
@lru_cache
def get_settings()->Settings:
    return Settings()

settings=get_settings()