import os

def video_to_audio(video_path, audio_path):
    command = f'ffmpeg -i {video_path} -ab 160k -ac 2 -ar 44100 -vn {audio_path}'
    os.system(command)