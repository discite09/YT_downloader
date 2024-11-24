from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import ffmpeg



def Get_video(url,path):
    if not os.path.exists(path): #directory check
        os.makedirs(path)
    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title)
    ys = yt.streams.filter().order_by("resolution").last() #get highist resolution

    before_files = set(os.listdir(path))
    print(before_files)
    ys.download(path)
    after_files = set(os.listdir(path))
    new_file = list(after_files - before_files)
    file_path = os.path.join(path, new_file[0])

    return file_path



def Get_sound(url,path):
    if not os.path.exists(path):
        os.makedirs(path)
    yt = YouTube(url, on_progress_callback = on_progress)
    ys = yt.streams.get_audio_only()

    before_files = set(os.listdir(path))
    ys.download(path)
    after_files = set(os.listdir(path))
    new_file = list(after_files - before_files)
    file_path = os.path.join(path, new_file[0])

    return file_path

def Merge(Audio_path,Video_path,Title):
    video = ffmpeg.input(Video_path)
    audio = ffmpeg.input(Audio_path)
    ffmpeg.output(video, audio,'gay.mp4').run(overwrite_output=True)





if __name__ == '__main__':
    Merge(Get_sound('https://www.youtube.com/watch?v=GPLImB-I71w','./downloads'),Get_video('https://www.youtube.com/watch?v=GPLImB-I71w','./downloads'),'./downloads')
   