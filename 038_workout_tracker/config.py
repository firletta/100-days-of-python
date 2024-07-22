import os
from dotenv import load_dotenv


load_dotenv()

NUTRITIONIX_API_ID = os.getenv("NUTRITIONIX_API_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
SHEETY_API_ENDPOINT = os.getenv("SHEETY_API_ENDPOINT")
SHEETY_API_TOKEN = os.getenv("SHEETY_API_TOKEN")
