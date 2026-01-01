import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

HF_TOKEN = os.getenv("HF_TOKEN")

class Settings:
    HF_TOKEN : str = os.getenv("HF_TOKEN")

    MODEL_ID: str = "google/gemma-3-12b-it"

settings = Settings()