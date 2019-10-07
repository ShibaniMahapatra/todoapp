import youtube_dl
import os
from flask import Flask
from flask import request
import shutil
import requests
from flask_restplus import Api,Resource


app = Flask(__name__)
url='http://www.youtube.com/watch?v=BaW_jenozKc'

api = Api(app=app)
ns_conf = api.namespace('youtube', description='youtube operations')

@ns_conf.route("/")
class youtube():
# @app.route("/youtube",methods = ["POST","GET","DELETE","PUT"])
    def youtube(self):
    # url = request.form.get("urlDownload")


        with youtube_dl.YoutubeDL({}) as ydl:
            # source = os.getcwd()
            # destination = '/home/shibani/Downloads/rough'
            # os.rename(source, destination)
            # p= ydl.download([url])
            # print(p)
            r = requests.get(url)
            print(r)
            # with open('/home/shibani/Downloads/rough', 'wb') as f:
            #     ydl.download([url])
            #     f.write(r.content)

        return "youtubeDone"

# cwd = os.getcwd()
# print(cwd)
# destination='/home/shibani/Downloads/rough'
# shutil.move(cwd, destination)
if __name__ == "__main__":
    app.run(debug=False)