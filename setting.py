from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    MONGO_URI:str
    GOOGLE_API_KEY:str

    model_config  = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', case_sensitive=True, extra='forbid')

settings = Setting()