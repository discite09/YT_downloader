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

    output_path = f'./downloads/{Title} done.mp4'
    ffmpeg.output(video, audio, output_path ).run(overwrite_output=True)





if __name__ == '__main__':
     url = input("Input URL :")
     title = YouTube(url).title
     print(title)
     path = './downloads' #temp

     while 1 :
         print("1.Video    2.Audio olny")
         mod = input("Select Mod :")

         if mod == '1':
             vid = Get_video(url,path)
             aud = Get_sound(url,path)
             Merge(aud,vid,title)

         elif mod == '2':
             Get_sound(url,path)
         
         else :
             print("mod dosn't exsist!")

        
         if input('continue?') == 'n' or 'N' :
             
             break;

   