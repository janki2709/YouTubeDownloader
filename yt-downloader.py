import youtube_dl

url = input("Please enter youtube video url :- \n")

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])