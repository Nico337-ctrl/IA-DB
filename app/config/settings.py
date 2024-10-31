import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SERVER_URL = os.getenv("SERVER_URL")
    OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

settings = Settings()
