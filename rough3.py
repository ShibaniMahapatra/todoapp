#importing the module
from pytube import YouTube

#where to save
SAVE_PATH = "/home/shibani/Downloads/rough" #to_do

#link of the video to be downloaded
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"


yt = YouTube(link)
#filters out all the files with "mp4" extension
mp4files = yt.filter('mp4')

yt.set_filename('GeeksforGeeks Video') #to set the name of the file

#get the video with the extension and resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
d_video.download(SAVE_PATH)

print('Task Completed!')
