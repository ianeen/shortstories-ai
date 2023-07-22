import openai_wrapper, voice_wrapper, video_maker
# import youtube_uploader
import requests
import shutil
import schedule
import time

from constants import *

def gen_story(channel, title_query, story_query, style, voice):
    title_answer = openai_wrapper.gpt3_short_run(title_query)
    print(f'{title_answer}\n')
    story_query = f'{story_query} {title_answer}.'
    story_answer = openai_wrapper.gpt3_long_run(story_query)
    split_answer = story_answer.split('.')
    split_answer.pop()
    urls = []
    line = 0
    for split in split_answer:
        split = split.lstrip(' ')
        split = split + '.'
        print(f'{split}')
        url = openai_wrapper.dalle_long_run(f'{style} {split}')
        urls.append(url)
        voice_wrapper.voice_run(split, voice, f'line{line}')

        r = requests.get(url, stream = True)
    
        with open(f'./short_story/res/line{line}.png','wb') as f:
            shutil.copyfileobj(r.raw, f)

        line = line + 1
    
    desc = f'Short {channel} story titled: {title_answer}.'
    
    return line, title_answer, desc

def start_flow():
    for story_type in TYPES:
        trying = True
        while (trying):
            channel = story_type.get('channel')
            title_query = story_type.get('title_query')
            story_query = story_type.get('story_query')
            art_style = story_type.get('art_style')
            voice = story_type.get('voice')
            try:
                lines, title, desc = gen_story(channel, title_query, story_query, art_style, voice)
            except:
                continue

            if video_maker.make_video(lines, channel):
                title = title.replace('"', '')
                # youtube_uploader.upload(title, desc, channel)
                trying = False

    print('Daily uploads completed... Wohoo')

def main():
    schedule.every().day.at('12:00').do(start_flow())
    while True:
        schedule.run_pending()
        time.sleep(600)

if __name__ == "__main__":
    # main()
    start_flow()
    