from json import JSONEncoder

from bson import ObjectId
from flask import Flask
from flask import request, url_for, redirect
from flask import render_template
import pymongo
import json
from datetime import datetime
from datetime import date
from collections import defaultdict



myclient = pymongo.MongoClient('mongodb://localhost:27017/')
tododb = myclient['dbtodo']
todocol = tododb["todotable"]
app = Flask(__name__)


taskList=[]
# dict1={}
dictReport = defaultdict(list)
# dict1 = dict()

@app.route("/todo",methods = ["POST","GET","DELETE","PUT"])
def insert():
    if request.method == 'POST':
        taskDict={}
        taskDict["created"] = request.form.get("createdAt")
        taskDict["scheduled"] = request.form.get("scheduledAt")
        taskDict["title"] = request.form.get("title")
        taskDict["description"] = request.form.get("description")
        taskDict["completed"] = request.form.get("completedAt")
        taskDict["lastUpdated"] = request.form.get("lastUpdatedAt")
        insertedResult = todocol.insert_one(taskDict)
        print((insertedResult))
        response = json.dumps({"success": "true", "status": 200, "result": "insertedResult"})
        # print(type(response))
        return response
    if request.method == 'GET':
        collection = todocol
        cursor = collection.find({})
        for document in cursor:
            document['_id'] = str(document['_id'])
            print(document)
            print(type(document))
            taskList.append(document)
        print(taskList)
        todojson = json.dumps(taskList)
        # json.encode(todojson, cls=JSONEncoder)
        return todojson

    if request.method=='DELETE':
        # myquery = {"_id": ObjectId("4d512b45cc9374271b02ec4f")}
        # todocol.delete_one(myquery)
        todocol.delete_one({"_id": ObjectId("5ccfd2003cb13401deb7af62x")})
        cursor = todocol.find({})
        for document in cursor:
            print(document)
        return "Done"
    # if request.method =='PUT':
    #     todocol.update({"_id": ObjectId("5cc4a2f79c44bf613aeaea4b")}, {'set': {"new_field": 1}})
    #     cursor = todocol.find({})
    #     for document in cursor:
    #         print(document)
    #     return "Doneput"


@app.route("/todoone",methods = ["POST","GET","DELETE","PUT"])
def insert_one():
    if request.method=='GET':
        for i in todocol.find({"_id": ObjectId("5ccf0926a62b0a04224b15f9")}):
            print(i)
        return "YES"
    if request.method=='DELETE':
        todocol.delete_many({})
        cursor = todocol.find({})
        for document in cursor:
            print(document)
        return "DeleteAllDone"
    if request.method =='PUT':
        todocol.update({'title': 'Title4'}, {"$set": {"scheduled": "20/07/2019"}})
        cursor = todocol.find({})
        for document in cursor:
            print(document)
        return "Doneput"


@app.route("/todoreport",methods = ["POST","GET","DELETE","PUT"])
def report():
    today=datetime.strptime(str(date.today()), '%Y-%m-%d')
    collection = todocol
    cursor = collection.find({})
    for document in cursor:
        # print(document)
        completed=(document['completed'])
        scheduled=(document['scheduled'])
        if(completed!=""):
            dictReport["completed"]=document
        else:
            scheduledDate = datetime.strptime(scheduled, '%d/%m/%Y')
            if scheduledDate < today:
                dictReport["backlog"] = document
            else:
                dictReport["pending"] = document
    print(dictReport)
    return "YES"

if __name__ == "__main__":
    app.run(debug=False)

