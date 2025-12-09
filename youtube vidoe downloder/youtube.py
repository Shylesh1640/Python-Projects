from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_resolution_stream = stream.highest_resolution()
        highest_resolution_stream.download(output_path=save_path)
        print(f"Download completed: {yt.title}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
url = input("Enter the YouTube video URL: ")
save_path = filedialog.askdirectory(title="Select Download Folder")
download_video(url, save_path)

    