from functools import lru_cache

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    pass


@lru_cache()
def get_settings() -> Settings:
    return Settings()