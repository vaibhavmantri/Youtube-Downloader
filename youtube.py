from pytube import YouTube
import os

def download(format,song):
    if format == "video" or format == "Video":
        print("Downloading....")
        yt.streams.get_highest_resolution().download()
    elif format == "audio" or format == "Audio":
        stream = yt.streams.filter(type='audio',only_audio=True)
        print(stream[0])
        stream[0].download()
        os.rename(stream[0].default_filename, song + '.mp3')
        print("Downloading....")
        stream[0].download()
# link = input("https://youtu.be/PJWemSzExXs")
link = input("Enter the link :- ")
yt = YouTube(link)

song = yt.title
print(song)

format = input("Enter the format you want the file to be in :- ")
download(format,song)

# location = input("Enter the location to be Saved :- " )
# ys = yt.streams.get_highest_resolution()


print("Download Complete")
