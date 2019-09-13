from flask import Flask
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

# app.expect(model)
@app.route("/todo", methods=["POST", "GET", "DELETE", "PUT"])
def GetCreateTodo():
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        print(data)
        output, status_code = todo_handler.create_todo(data)
        if status_code == 200:
            response = str(json.dumps({"success": "true", "status": status_code, "message": output}))
        else:
            response = str(json.dumps({"success": "false", "status": status_code, "message": output}))
        return response
