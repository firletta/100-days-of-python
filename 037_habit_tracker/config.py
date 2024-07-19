import os
from dotenv import load_dotenv


load_dotenv()

PIXELA_API_TOKEN = os.getenv("PIXELA_API_TOKEN")
PIXELA_API_USERNAME = os.getenv("PIXELA_API_USERNAME")