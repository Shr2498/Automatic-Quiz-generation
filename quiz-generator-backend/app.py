# TODO: Restructure project

from flask import Flask, request
from openai import AsyncOpenAI
from os import environ
from json import loads as str_to_json

app = Flask(__name__)

# Get API Key
api_key = environ.get("OPENAI_API_KEY")
if api_key is None:
    print("OpenAI API key is missing")
    exit(1)

# Set up client
openai_client = AsyncOpenAI(api_key=api_key)

@app.route("/generate", methods=['POST'])
async def main():
    print(request.form)
    questions = await ask_gpt("Generate 10 multiple choice questions in a JSON format")
    return questions



async def ask_gpt(prompt: str) -> str:
    completion =  await openai_client.chat.completions.create(
        # response_format={ "type": "json_object" },
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return str(completion.choices[0].message.content)
