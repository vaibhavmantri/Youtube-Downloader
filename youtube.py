from pytube import YouTube
import moviepy.editor as mp

def download(format):
    if format == "video" or format == "Video":
        print("Downloading....")
        yt.streams.get_highest_resolution().download()
    elif format == "audio" or format == "Audio":
        stream = yt.streams.filter(only_audio=True).all()
        print("Downloading....")
        stream[0].download()
# link = input("https://youtu.be/PJWemSzExXs")
# link = input("Enter the link :- ")
yt = YouTube("https://www.youtube.com/watch?v=SD5EwigRcNg")

song = yt.title
print(song)

format = input("Enter the format you want the file to be in :- ")
download(format)

# location = input("Enter the location to be Saved :- " )
# ys = yt.streams.get_highest_resolution()


print("Download Complete")
