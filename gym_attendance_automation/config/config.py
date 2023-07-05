from pydantic import BaseSettings


class Settings(BaseSettings):
    ICLOUD_EMAIL: str
    ICLOUD_PASSWORD: str
    
    class Config:
        env_file = ".env"


settings = Settings()
