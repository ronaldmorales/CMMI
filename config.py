# config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
  JWT_SECRET_KEY: str
  JWT_ALGORITHM: str
  ACCESS_TOKEN_EXPIRE_MINUTES: int

  class Config:
  env_file = ".env"

settings = Settings()
