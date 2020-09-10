import tkinter as tk
from pytube import YouTube
import os

# Label Field
master = tk.Tk()
tk.Label(master, text="Link of the Youtube Video").grid(row=0)

# Entry Field
e1 = tk.Entry(master)
e1.grid(row=0, column=1)

# Function for Downloading
def download(link):
    yt = YouTube(link)
    song = yt.title
    stream = yt.streams.filter(type='audio',only_audio=True)
    print(stream[0])
    stream[0].download()
    #Convert the Present mp4 Audio preset to mp3 extension
    os.rename(stream[0].default_filename, song + '.mp3')
    print("Downloading....")
    stream[0].download()
    print("Download Complete...!")

def printing(value):
    print(e1.get())
    download(e1.get())

radbtn = tk.Radiobutton(master,text = "Helleww!", value = 1,variable = "radbtn1")
radbtn.grid(row = 1, column = 1)

# Button for Confirmation
button = tk.Button(master, text = "Download!", command = printing)
button.grid(row = 1,column = 0)
master.mainloop()

