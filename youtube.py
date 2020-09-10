from pytube import YouTube
import os
import tkinter as tk

def download(format,song):
    # If you want Video..
    if format == "video" or format == "Video":
        print("Downloading....")
        yt.streams.get_highest_resolution().download()
    # If you want Audio only.
    elif format == "audio" or format == "Audio":
        stream = yt.streams.filter(type='audio',only_audio=True)
        print(stream[0])
        stream[0].download()
        #Convert the Present mp4 Audio preset to mp3 extension
        os.rename(stream[0].default_filename, song + '.mp3')
        print("Downloading....")
        stream[0].download()

# Provide the link
# link = input("Enter the link :- ")
yt = YouTube("https://www.youtube.com/watch?v=Yv3MvtdS5Pw&list=RDMMYv3MvtdS5Pw&index=1")

# Determines the Title of the song
song = yt.title
print(song)

format = input("Enter the format you want the file to be in :- ")
download(format,song)


print("Download Complete")
