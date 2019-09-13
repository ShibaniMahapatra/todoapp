from flask import Flask
from flask import request
import pymongo
from bson import ObjectId
import json

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
tododb = myclient['dbtodo']
todocol = tododb['todotable']
app = Flask(__name__)
@app.route("/todo_one/<string:id>",methods = ["POST","GET","DELETE","PUT"])
def method(id):
    data={"created": "10/02/2019",
          "scheduled": "01/09/2019",
          "title": "title11",
          "description": "Hello world2",
          "completed": "03/09/2019",
          "lastUpdated": "30/04/2019"
          }
    if request.method == 'PUT':
        todocol.update({'_id': ObjectId(id)},{"$set": data})
        cursor = todocol.find({})
        for document in cursor:
            print(document)
        return "Doneput"


if __name__ == "__main__":
    app.run(debug=False)