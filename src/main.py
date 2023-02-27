import telebot
import os
from dotenv import load_dotenv
from AI_API_Handler.ai_handler import make_a_question

load_dotenv()

TELEGRAM_API_KEY = os.getenv("TELEGRAM_KEY")
bot = telebot.TeleBot(str(TELEGRAM_API_KEY))
