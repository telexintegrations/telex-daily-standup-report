import secrets
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  PROJECT_NAME: str = "telex-daily-standup-report"
  PROJECT_VERSION: str = "0.0.1"
  PROJECT_DESCRIPTION: str = "This Telex integration sends a scheduled reminder to a channel, prompting team members to submit their daily standup reports."
  API_PREFIX: str = "/api/v1"
  SECRET_KEY: str = secrets.token_urlsafe(32)
  DEBUG: bool = False
  TESTING: bool = False

settings = Settings()
