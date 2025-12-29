from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Algerian Print-on-Demand Platform"
    API_V1_STR: str = "/api/v1"

    # Database settings
    DATABASE_URL: str = "postgresql://user:password@localhost/algerian_print"

    # JWT settings
    SECRET_KEY: str = "a_very_secret_key"  # Replace with a real secret key
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")

settings = Settings()
