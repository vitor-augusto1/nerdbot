import json
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('TELEGRAM_API_KEY')
