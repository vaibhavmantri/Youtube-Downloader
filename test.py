from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=SD5EwigRcNg&list=RD6I-4m-hMIOE&index=8")
stream = yt.streams.filter(type='audio',only_audio=True)
print(stream[0])
stream[0].download()