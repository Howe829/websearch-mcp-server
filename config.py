from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    bing_search_base_url: str
    google_search_base_url: str
    cc: str
    language: str
    impersonate: str
    host: str
    port: int
    server_mode: str
    llm_base_url: str
    llm_api_key: str
    llm_model_name: str


settings = Settings()
