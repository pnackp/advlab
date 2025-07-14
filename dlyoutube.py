# pip install yt_dlp

import yt_dlp #import lib 
def download_youtube_video(url, save_path="."):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s', # save path is where you need to intall at , title is title video . ext is extension file
        'format': 'best' #set download highest quality
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
video_url = input("Enter the YouTube video URL: ") #enter url and keep it in variable video_url;
download_youtube_video(video_url, save_path=".")#call function and sent url , and path you need to save at
