from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    postgres_uri: str = os.getenv("SUPABASE_URL")    
    
settings = Settings()