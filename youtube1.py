import youtube_dl
import os
from flask import Flask
from flask import request
import shutil


app = Flask(__name__)

url='http://www.youtube.com/watch?v=BaW_jenozKc'
@app.route("/youtube",methods = ["POST","GET","DELETE","PUT"])
def youtube():
    # url = request.form.get("urlDownload")


    with youtube_dl.YoutubeDL({}) as ydl:
        # source = os.getcwd()
        # destination = '/home/shibani/Downloads/rough'
        # os.rename(source, destination)
        ydl.download([url])
    return "youtubeDone"

# cwd = os.getcwd()
# print(cwd)
# destination='/home/shibani/Downloads/rough'
# shutil.move(cwd, destination)
if __name__ == "__main__":
    app.run(debug=False)