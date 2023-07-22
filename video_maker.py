from constants import *
from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips, vfx

def make_video(lines, channel):
    clips = []

    for line in range(lines):
        audio_clip = AudioFileClip(f'./short_story/res/line{line}.mp3')
        image_clip = ImageClip(f'./short_story/res/line{line}.png').set_duration(audio_clip.duration)
        video_clip = image_clip.set_audio(audio_clip).set_end(audio_clip.duration-0.1)
        video_clip.fps = 1
        clips.append(video_clip)

    final_video = concatenate_videoclips(
        clips,
        method="compose"
    )

    final_duration = final_video.duration
    if final_duration < 70:
        if final_duration >= 60:
            final_video = final_video.fx(vfx.speedx, 1+((final_duration-59)/59))
    else:
        return False

    final_video.write_videofile(f'./short_story/res/{channel}.mp4', fps=1, ffmpeg_params=['-lavfi', BLUR_ATTRIBUTE])
    return True
