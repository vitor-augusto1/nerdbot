import json
import openai
from dotenv import load_dotenv
from dataclasses import dataclass
import os

load_dotenv()
openai.api_key = os.getenv('TELEGRAM_API_KEY')


@dataclass
class OpenAiRequestHeaders:
    model: str
    prompt: str
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: int

def return_ai_response(open_ai_headers: OpenAiRequestHeaders) -> str:
    """Return openAI api response or error message."""
    try:
        response = openai.Completion.create(**vars(open_ai_headers))
        json_object_response = json.loads(str(response))
        AI_answer = json_object_response["choices"][0]["text"]
        empty_string = ""
        if AI_answer == empty_string  or AI_answer == " ":
            error_message = (
                f"Não foi possivel gerar uma resposta. Tente novamente!"
            )
            return error_message
        return AI_answer
    except openai.error.RateLimitError as error:
        return "Erro ao gerar resposta. Tente novamente."


def answer_user_question(alternatives: str) -> str:
    """Return ai answer."""
    headers = OpenAiRequestHeaders(
      model="text-davinci-003",
      prompt=alternatives.strip(),
      temperature=0.2,
      max_tokens=3000,
      top_p=1,
      frequency_penalty=0.2,
      presence_penalty=0
    )
    response = return_ai_response(headers)
    return response


def summarize_text(text: str) -> str:
    """Return ai answer."""
    headers = OpenAiRequestHeaders(
      model="text-davinci-003",
      prompt=f"{text}.\n\nTl;dr",
      temperature=0.7,
      max_tokens=170,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=1
    )
    response = return_ai_response(headers)
    return response
