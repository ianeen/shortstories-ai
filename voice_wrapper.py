import requests
import json
import base64

from constants import *

def voice_run(text, voice, filename):
    body = {'text': text, 'voice': voice}

    trying = True
    while (trying):
        response = requests.post(VOICE_URL, json = body)

        json_res = response.json()
        data = json_res.get('data')
        if data:
            b64data = base64.b64decode(data)

            with open(f'./short_story/res/{filename}.mp3', 'wb') as out:
                out.write(b64data)
                trying = False
