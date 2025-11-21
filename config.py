import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file automatically

HF_TOKEN = os.getenv("HF_TOKEN")
