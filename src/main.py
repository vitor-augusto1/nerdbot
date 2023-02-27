import telebot
import os
from dotenv import load_dotenv
from AI_API_Handler.ai_handler import make_a_question

load_dotenv()

TELEGRAM_API_KEY = os.getenv("TELEGRAM_KEY")
bot = telebot.TeleBot(str(TELEGRAM_API_KEY))

@bot.message_handler(commands=['start'])
def start_message(message) -> None:
    CHAT_ID = message.chat.id
    bot.send_message(CHAT_ID, "Hello, world!")

