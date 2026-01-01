import os
from pathlib import Path
from dotenv import load_dotenv

# 1. Define the path logic outside
try:
    _BASE_DIR = Path(__file__).resolve().parent.parent
except NameError:
    _BASE_DIR = Path(os.getcwd())

# 2. Load the .env file
load_dotenv(_BASE_DIR / ".env")

class Settings:
    # 3. Now include it as an attribute of the class
    BASE_DIR: Path = _BASE_DIR
    HF_TOKEN: str = os.getenv("HF_TOKEN")
    MODEL_ID: str = "meta-llama/Llama-3.1-8B-Instruct"

settings = Settings()

if not settings.HF_TOKEN:
    print("ERROR: HF_TOKEN is empty! Check your .env file location.")