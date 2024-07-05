import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import (PostgresDsn, ValidationError, ValidationInfo,
                      field_validator)
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    CONNECTION_SCHEMA: Optional[PostgresDsn] = None

    AWS_KEY: Optional[str] = None
    AWS_SECRET: Optional[str] = None

    @field_validator("CONNECTION_SCHEMA")
    def database_schema(cls, _: str, info: ValidationInfo):
        schema = {
            "scheme": "postgresql",
            "username": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "host": os.getenv("DB_HOST"),
            "port": 5432,
            "path": "",
        }

        if not schema:
            raise ValidationError("Database schema is not set")

        return PostgresDsn.build(**schema)

    @field_validator("AWS_KEY")
    def get_key(cls, _: str):
        key = os.getenv("AWS_KEY")
        if not key:
            raise ValidationError("AWS_KEY is not set")
        return key

    @field_validator("AWS_SECRET")
    def get_secret(cls, _: str):
        secret = os.getenv("AWS_SECRET")
        if not secret:
            raise ValidationError("AWS_SECRET is not set")
        return secret


settings = Settings()
