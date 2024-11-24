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
    video_file = ys.download(path)

    #merge sound
    audio_file = Get_sound(url,path)
    output_file = path
    ffmpeg.input(video_file).output(audio_file).output(output_file, vcodec='copy', acodec='aac').run()



def Get_sound(url,path):
    if not os.path.exists(path):
        os.makedirs(path)
    yt = YouTube(url, on_progress_callback = on_progress)
    ys = yt.streams.get_audio_only()
    ys.download(path)



if __name__ == '__main__':
    path = input("Select Save path :")
    while 0:
        url = input("Video Url:")

