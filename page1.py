# import sqlalchemy
import pymongo
from flask import Flask
from requests import Session

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
tododb = myclient['dbtodo']
todocol = tododb['todotable']

app = Flask(__name__)


@app.route("/page/<int:limit>/<int:offset>",methods = ["POST","GET","DELETE","PUT"])
# @app.route("/todo_one/<string:id>",methods = ["POST","GET","DELETE","PUT"])

def page(limit,offset):
    print("hello")
    for data in todocol.find({}).limit(limit).skip(offset):
        print(data)
    return "hello"

if __name__ == "__main__":
    app.run(debug=False)


# @app.route("/todo",methods = ["POST","GET","DELETE","PUT"])
