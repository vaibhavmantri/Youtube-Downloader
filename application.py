import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Label Field
master = tk.Tk()
master.title("Youtube Downloader")
master.geometry('1000x500')
tk.Label(master, text="Link of the Youtube Video").grid(row=0)

# Entry Field
e1 = tk.Entry(master)
e1.grid(row=0, column=1)


text = tk.Text(master)
text.grid(row = 2,column = 1)

# Function for Downloading
def download(link,format_choosen):
    yt = YouTube(link)
    song = yt.title
    print(yt.title)
    text.insert(tk.INSERT,yt.title)
    text.insert(tk.INSERT,"\nDownloading.....")
    print(format_choosen) 
    if format_choosen == 0:
        # stream = yt.streams.filter(res = "1080p")
        print("Downloading....")
        # stream[0].download()
        join_audio_video(song,yt)
    elif format_choosen == 1:
        stream = yt.streams.filter(res = "720p")
        print("Downloading....")
        stream[0].download()
    elif format_choosen == 2:
        stream = yt.streams.filter(res = "480p")
        print("Downloading....")
        stream[0].download()
    elif format_choosen == 3:
        stream = yt.streams.filter(res = "360p")
        print("Downloading....")
        stream[0].download()
    elif format_choosen == 4:
        stream = yt.streams.filter(res = "240p")
        print("Downloading....")
        stream[0].download()
    elif format_choosen == 5:
        stream = yt.streams.filter(res = "144p")
        print("Downloading....")
        stream[0].download()
    elif format_choosen == 6:
        stream = yt.streams.filter(type='audio',only_audio=True)
        print(stream[0])
        stream[0].download()
        
        #Convert the Present mp4 Audio preset to mp3 extension
        os.rename(stream[0].default_filename, song + '.mp3')
        print("Downloading....")
        stream[0].download()
        os.remove(song + '.mp4')
    print("Download Complete...!")
    text.insert(tk.INSERT, "\nDownload Complete......!")
    
def join_audio_video(song,yt):
    download_video(song,yt)
    download_audio(song,yt)
    
    clip1 = VideoFileClip("2.mp4")
    clip2 = VideoFileClip("1.mp3")
    final_clip = concatenate_videoclips([clip1,clip2])
    final_clip.write_videofile(".mp4")

def download_video(song, yt):
    stream = yt.streams.filter(res = "1080p")
    stream[0].download()
    os.rename(song + ".mp4", "2.mp4")



def download_audio(song,yt):
    stream = yt.streams.filter(type='audio',only_audio=True)
    print(stream[0])
    stream[0].download()
    #Convert the Present mp4 Audio preset to mp3 extension
    os.rename(stream[0].default_filename,'1' + '.mp3')
    print("Downloading....")
    stream[0].download()
    return 0

def printing():
    print(e1.get())
    download(e1.get(),format_choosen.current())

#Dropdown Format
x = tk.StringVar()
format_choosen = ttk.Combobox(master,width = '7', textvariable = x)
format_choosen['values'] = (
                                '1080p',
                                '720p',
                                '480p',
                                '360p',
                                '240p',
                                '144p',
                                'mp3')
format_choosen.grid(row = 1, column = 1)
format_choosen.current(0)

# Button for Confirmation
button = tk.Button(master, text = "Download!", command = printing)
button.grid(row = 2,column = 1)
master.mainloop()

