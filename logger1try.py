from flask import Flask, Response
import requests
import logging
from logging.handlers import RotatingFileHandler

from flask import request, url_for, redirect
from flask import render_template
import pymongo
import json
from datetime import datetime
from datetime import date
from collections import defaultdict
from todo_handler import TodoHandler
from bson import ObjectId


myclient = pymongo.MongoClient('mongodb://localhost:27017/')
tododb = myclient['dbtodo']
todocol = tododb['todotable']
app = Flask(__name__)

# dict1={}
dictReport = defaultdict(list)
todo_handler = TodoHandler()

@app.route("/todo",methods = ["POST","GET","DELETE","PUT"])
def GetCreateTodo():
    if request.method == 'GET':
        data = None
        output, status_code = todo_handler.get_todo(data)
        if status_code == 200:
            response = json.dumps({"success": "true", "status": status_code, "message": output})
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.info("%(asctime)s %s info %s")
        else:
            response = json.dumps({"success": "false", "status": status_code, "message": output})
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.info("(asctime)s %s error %s ")



        # file_handler = RotatingFileHandler('python.log', level=logging.DEBUG,maxBytes=1024 * 1024 * 100, backupCount=20)
        # file_handler.setLevel(logging.INFO)
        # formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # file_handler.setFormatter(formatter)
        # app.logger.addHandler(file_handler)


        # return response
        # app.logger.warning('testing warning log')
        # app.logger.error('testing error log')
        # app.logger.info('testing info log')
        return response
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        print(data)
        output, status_code = todo_handler.create_todo(data)
        if status_code == 200:
            response = (json.dumps({"success": "true", "status": status_code, "message": output}))
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.info("(asctime)s %s info %s ")
            # resp = requests.Session().send(response)
            # return (resp.text, resp.status_code)

            print(type(response))
            return Response(status=200, response=response)
            # return response,200

        else:
            response = (json.dumps({"success": "false", "status": status_code, "message": output}))
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.info("(asctime)s %s error %s ")
            # resp = requests.Session().send(response)
            # return (resp.text, resp.status_code)
            return Response(status=400,response=response)

            # return response,400

if __name__ == "__main__":
    # app.run(debug=False)
    # handler = RotatingFileHandler('info.log', maxBytes=1000, backupCount=1)
    # handler.setLevel(logging.INFO)
    #
    # handler = logging.StreamHandler()
    # log_format = "%(asctime)s\t%(message)s"
    # formatter = logging.Formatter(log_format)
    # handler.setFormatter(formatter)
    # app.logger.addHandler(handler)
    # #
    # # # set the app logger level
    # # app.logger.setLevel(logging.INFO)
    #
    # # app.logger.addHandler(handler)
    app.run()
