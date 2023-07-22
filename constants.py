ADVENTURE = {
    'channel': 'adventure',
    'title_query': 'Generate a scary short story title for me.',
    'story_query': 'Tell me a scary short story under 220 words with the title',
    'art_style': 'Fantasy painting style (obscure faces)',
    'voice': 'en_us_007'
}

MYSTERY = {
    'channel': 'mystery',
    'title_query': 'Generate a mysterious short story title for me.',
    'story_query': 'Tell me a mysterious short story under 220 words with the title',
    'art_style': 'Grey watercolor style (obscure faces):',
    'voice': 'en_uk_001'
}

SCARY = {
    'channel': 'scary',
    'title_query': 'Generate a mysterious short story title for me.',
    'story_query': 'Tell me a mysterious short story under 220 words with the title',
    'art_style': 'Black and white painting style (obscure faces):',
    'voice': 'en_us_ghostface'
}

HAPPY = {
    'channel': 'happy',
    'title_query': 'Generate a happy short story title for me.',
    'story_query': 'Tell me a happy short story under 220 words with the title',
    'art_style': 'Impressionism style (obscure faces):',
    'voice': 'en_au_002'
}

# TYPES = [ADVENTURE, MYSTERY, SCARY, HAPPY]
TYPES = [MYSTERY]

BLUR_ATTRIBUTE = '[0:v]scale=iw*16/9:-1,boxblur=luma_radius=min(h\,w)/14:luma_power=1:chroma_radius=min(cw\,ch)/14:chroma_power=1[bg];[bg][0:v]overlay=(W-w)/2:(H-h)/2,crop=w=ih*9/16'

VOICE_URL = 'https://tiktok-tts.weilnet.workers.dev/api/generation'
