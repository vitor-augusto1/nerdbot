import json
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('TELEGRAM_API_KEY')

def make_a_question(user_question: str) -> str:
    user_question_formated = user_question.strip()
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Q: {user_question_formated}?\nA:",
      temperature=0.7,
      max_tokens=3000,
      top_p=1,
      best_of=2,
      frequency_penalty=0.7,
      presence_penalty=0,
      stop=["\n"]
    )
    json_object_response = json.loads(str(response))
    AI_answer = json_object_response["choices"][0]["text"]
    return AI_answer
