import openai
import os
from config import Config

openai.api_key = Config.OPENAI_API_KEY
def askGPT(text):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 150,
        
    )
    return response.choices[0].text
