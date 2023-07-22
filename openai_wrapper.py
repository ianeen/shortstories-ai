import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def gpt3_short_run(query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        max_tokens=256,
        temperature=0.9,
        top_p=1
    )
    json_res = json.loads(str(response))
    answer = json_res.get('choices')[0].get('text').replace('\n', '')
    return answer


def gpt3_long_run(query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        max_tokens=1024,
        temperature=0.8,
        top_p=1
    )
    json_res = json.loads(str(response))
    answer = json_res.get('choices')[0].get('text').replace('\n', '')
    return answer

def dalle_short_run(query):
    response = openai.Image.create(
        prompt=query,
        n=1,
        size="512x512"
    )
    json_res = json.loads(str(response))
    answer = json_res.get('data')[0].get('url')
    return answer

def dalle_long_run(query):
    response = openai.Image.create(
        prompt=query,
        n=1,
        size="1024x1024"
    )
    json_res = json.loads(str(response))
    answer = json_res.get('data')[0].get('url')
    return answer
