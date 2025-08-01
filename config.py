# config.py

import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
API_BEARER_TOKEN = os.getenv("API_BEARER_TOKEN", "932d887435ea59d029c2e1a6844a0590c534c3601c926ebf8847bdf608547a0d")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not set. Please update your .env file.")
