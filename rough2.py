import youtube_dl


ydl_opts = {'forcefilename':'True','outtmpl': '/home/shibani/Downloads/rough/filename1'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    p=ydl.download(['https://www.youtube.com/watch?v=xWOoBJUqlbI'])
    print(p)
    print(ydl)
