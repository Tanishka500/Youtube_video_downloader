from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive = True, file_extension = "mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path = save_path)
        print("Video downloaded successfully")
    except Exception as e:
        print(e)

url = "https://youtu.be/lDi0SbwwtMw?si=jfFiZiV5QQYc-XbS"
save_path = "D:\practice\Youtube video downloader"

download_video(url,save_path)