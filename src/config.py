from pydantic_settings import BaseSettings
#from pydantic import BaseSettings
import os.path

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    # class Config:
    #     env_file = ".env"

    class Config:
        env_file = f"{os.path.dirname(os.path.abspath(__file__))}/.env"

settings = Settings()
