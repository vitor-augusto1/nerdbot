import json
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('TELEGRAM_API_KEY')

def answer_user_question(alternatives: str) -> str:
    try:
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt=alternatives.strip(),
          temperature=0.2,
          max_tokens=3000,
          top_p=1,
          frequency_penalty=0.2,
          presence_penalty=0
        )
        print(response)
        json_object_response = json.loads(str(response))
        AI_answer = json_object_response["choices"][0]["text"]
        empty_string = ""
        if AI_answer == empty_string or AI_answer == " ":
            error_message = (
                f"Não foi possivel escolher uma alternativa. Tente novamente!"
            )
            return error_message
        return AI_answer
    except openai.error.RateLimitError as e:
        return "Erro ao gerar resposta. Tente novamente."


def summarize_text(text: str) -> str:
    try:
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt=f"{text}.\n\nTl;dr",
          temperature=0.7,
          max_tokens=60,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=1
        )
        json_object_response = json.loads(str(response))
        AI_answer = json_object_response["choices"][0]["text"]
        empty_string = ""
        if AI_answer == empty_string or AI_answer == " ":
            error_message = (
                f"Não foi possivel escolher uma alternativa. Tente novamente!"
            )
            return error_message
        return AI_answer
    except openai.error.RateLimitError as e:
        return "Erro ao gerar resposta. Tente novamente."
