from pytube import YouTube
import os

link = input("Enter the link :- ")
yt = YouTube(link)
stream = yt.streams.filter(type='audio',only_audio=True)
print(stream[0])
stream[0].download()
os.rename(stream[0].default_filename, 'baarishein.mp3')