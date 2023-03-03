import telebot
import os
from dotenv import load_dotenv
from AI_API_Handler.ai_handler import answer_user_question, summarize_text

load_dotenv()

TELEGRAM_API_KEY = os.getenv("TELEGRAM_KEY")
bot = telebot.TeleBot(str(TELEGRAM_API_KEY))


@bot.message_handler(commands=['start'])
def start_message(message) -> None:
    CHAT_ID = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                 one_time_keyboard=False)
    keyboard.row('/question', '/summary', '/helper')
    user_guide_message = (
        f'Bem vindo ao NerdBot ! \n'
        f'Escreva ou aperte um dos botões que aparecem no seu teclado.'
    )
    bot.send_message(CHAT_ID, user_guide_message, reply_markup=keyboard)


@bot.message_handler(commands=['helper'])
def show_user_guide(message) -> None:
    CHAT_ID = message.chat.id
    user_guide_message = (
        f'/question : Responde pergunta feita pelo usuário.\n'
        f'/summary : Resume textos.'
    )
    bot.send_message(CHAT_ID, user_guide_message)


@bot.message_handler(commands=['question'])
def answer_a_question(message) -> None:
    CHAT_ID = message.chat.id
    message_to_user = (
        "Me mande a sua pergunta."
    )
    user_question = bot.send_message(CHAT_ID, message_to_user)
    bot.register_next_step_handler(user_question, send_the_alternative)

def send_the_alternative(message) -> None:
    CHAT_ID = message.chat.id
    ai_answer = answer_user_question(message.text)
    bot.send_message(CHAT_ID, ai_answer)


@bot.message_handler(commands=['summary'])
def summarize_user_text(message) -> None:
    CHAT_ID = message.chat.id
    message_to_user = (
        f"Me envie o texto para ser resumido."
    )
    user_text = bot.send_message(CHAT_ID, message_to_user)
    bot.register_next_step_handler(user_text, return_summary)

def return_summary(message):
    CHAT_ID = message.chat.id
    ai_answer = summarize_text(message.text)
    bot.send_message(CHAT_ID, ai_answer)


bot.infinity_polling()
