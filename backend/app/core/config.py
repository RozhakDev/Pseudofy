from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    """
    Mendefinisikan semua environment variables yang dibutuhkan oleh aplikasi.
    Pydantic akan otomatis membaca variabel dari file .env.
    """
    OPENROUTER_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), '..', '..', '.env'),
        env_file_encoding='utf-8'
    )

settings = Settings()