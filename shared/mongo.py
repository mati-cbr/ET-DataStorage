import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import AsyncMongoClient


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

client = AsyncMongoClient(os.environ.get("MONGODB_URL"))
