from pytube import YouTube
# link = input("https://youtu.be/PJWemSzExXs")
# link = input("Enter the link :- ")
yt = YouTube("https://www.youtube.com/watch?v=SD5EwigRcNg")

song = yt.title
print(song)


# print(stream)
format = input("Enter the format you want the file to be in :- ")
if format == "video" or format == "Vidio":
    print("Downloading....")
    yt.streams.get_highest_resolution().download()
elif format == "audio" or format == "Audio":
    stream = yt.streams.filter(only_audio=True).all()
    print("Downloading....")
    stream[0].downloads()

# location = input("Enter the location to be Saved :- " )
# ys = yt.streams.get_highest_resolution()


print("Download Complete")
