from json import JSONEncoder
import logging
from flask.views import MethodView
from flask import Flask, Response
from flask import request, url_for, redirect
from flask import render_template
import pymongo
import json
from datetime import datetime
from datetime import date
from collections import defaultdict
from todo_handler import TodoHandler
from bson import ObjectId
from flask_restplus import Api,Resource,fields

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
tododb = myclient['dbtodo']
todocol = tododb['todotable']
app = Flask(__name__)

# dict1={}
dictReport = defaultdict(list)
todo_handler = TodoHandler()

api = Api(app=app)
ns_conf = api.namespace('todo', description='todo operations')

model = api.model('todo',
		{'created': fields.String(required = True,description="Name of the person"),
        'title': fields.String(required = True,description="title of the person"),
        'scheduled': fields.String(required = True,description="sch of the person"),
        'completed': fields.String(required = True,description="comp of the person"),
        'description': fields.String(required = True,description="desc of the person"),
        'lastupdated': fields.String(required = True,description="lastupdate of the person")}
                  )



# @api.model(fields={'created': fields.String, 'title': fields.String,
#                    'scheduled': fields.String,'completed': fields.String,
#                    'description': fields.String,'lastupdated': fields.String})
# class Person(fields.Raw):
#     def format(self, value):
#         return {'created': value.created, 'title': value.title,
#                 'scheduled': value.scheduled,'completed': value.completed,
#                 'description': value.description,'lastupdated': value.lastupdated}


@ns_conf.route("/")
class todo(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument'})
    @api.expect(model)
    def post(self):
        # if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        print(data)
        output, status_code = todo_handler.create_todo(data)
        if status_code == 200:
            response = str(json.dumps({"success": "true", "status": status_code, "message": output}))
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.info("%(asctime)s %s post info %s")
            return Response(status=200, response=response)

        else:
            response = str(json.dumps({"success": "false", "status": status_code, "message": output}))
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.info("(asctime)s %s post error %s ")

            # taskDict={}
            # taskDict["created"] = request.form.get("createdAt")
            # taskDict["scheduled"] = request.form.get("scheduledAt")
            # taskDict["title"] = request.form.get("title")
            # taskDict["description"] = request.form.get("description")
            # taskDict["completed"] = request.form.get("completedAt")
            # taskDict["lastUpdated"] = request.form.get("lastUpdatedAt")
            # insertedResult = todocol.insert_one(taskDict)
            # print((insertedResult))
            # response = json.dumps({"success": "true", "status": 200, "result": "insertedResult"})
            # # print(type(response))
            # return response
    def get(self):
            # if request.method == 'GET':
            data = None
            output, status_code = todo_handler.get_todo(data)
            if status_code == 200:
                response = json.dumps({"success": "true", "status": status_code, "message": output})
                logging.basicConfig(filename='example.log', level=logging.DEBUG)
                logging.info("get info")
                return Response(status=200, response=response)

            else:
                response = json.dumps({"success": "false", "status": status_code, "message": output})
                logging.basicConfig(filename='example.log', level=logging.DEBUG)
                logging.info("get error")
                return Response(status=400, response=response)



            # cursor = todocol.find({})
            # for document in cursor:
            #     document['_id'] = str(document['_id'])
            #     taskList.append(document)
            # # print(taskList)
            # todojson = json.dumps(taskList)
            # # json.encode(todojson, cls=JSONEncoder)
            # return todojson
    def delete(self):
        # if request.method=='DELETE':
        output, status_code = todo_handler.delete_todo()
        if status_code == 200:
            response = json.dumps({"success": "true", "status": status_code, "message": output})
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.info("delete info")
            return Response(status=200, response=response)

        else:
            response = json.dumps({"success": "false", "status": status_code, "message": output})
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.info("delete error ")
            return Response(status=400, response=response)

            # todocol.delete_many({})
            # cursor = todocol.find({})
            # for document in cursor:
            #     print(document)
            # return "DeleteAllDone"


@ns_conf.route("/<string:id>")
class todo_one(Resource):
    def get(self,id):
        # if request.method=='GET':
        data = {"id": id}
        output, status_code = todo_handler.get_todo(data)
        if status_code == 200:
            response = json.dumps({"success": "true", "status": status_code, "message": output})
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.info("getone info %s")
            return Response(status=200, response=response)

        else:
            response = json.dumps({"success": "false", "status": status_code, "message": output})
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.info("getone error")
            return Response(status=400, response=response)

            # id=input("enter id")
            # for i in todocol.find({"_id": ObjectId(id)}):
            #     print(i)
            # return "YES"
            # print(output)

    def delete(self, id):
        # if request.method=='DELETE':
        data = {"id": id}
        output, status_code = todo_handler.delete_todo(data)
        if status_code == 200:
            response = json.dumps({"success": "true", "status": status_code, "message": output})
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.info("deleteone info ")
            return Response(status=200, response=response)

        else:
            response = json.dumps({"success": "false", "status": status_code, "message": output})
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.info("delete one error")
            return Response(status=400, response=response)

            # myquery = {"_id": ObjectId("4d512b45cc9374271b02ec4f")}
            # todocol.delete_one(myquery)
            # todocol.delete_one({"_id": ObjectId("5ccfd2003cb13401deb7af62x")})
            # cursor = todocol.find({})
            # for document in cursor:k
            #     print(document)
            # return "Done"

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument'})
    @api.expect(model)
    def put(self,id):
        # if request.method =='PUT':
        data = json.loads(request.data.decode('utf-8'))
        print(data)
        flag = 0
        collection = todocol
        cursor = collection.find({})
        for document in cursor:
            # print(document.values())
            if ObjectId(id) in document.values():
                print("yes")
                flag = 1
                todocol.update({'_id': ObjectId(id)}, {"$set": {"created": data["created"],
                                                                    "title": data["title"],
                                                                "scheduled": data["scheduled"],
                                                                "completed": data["completed"],
                                                                "description": data["description"],
                                                                "lastupdated": data["lastupdated"]}})
                print(document)
                response = json.dumps({"success": "true", "status": 200, "message": "Data Updated"})
                logging.basicConfig(filename='example.log', level=logging.DEBUG)
                logging.info("put info ")
                return Response(status=200, response=response)

        if flag == 0:
            response = json.dumps({"success": "false", "status": 400, "message": "Data Not Updated, Id not present"})
            return Response(status=400, response=response)


# @ns_conf.route("/report")
# # @app.route("/todoreport",methods = ["POST","GET","DELETE","PUT"])
# class report():
#     def report(self):
#         today=datetime.strptime(str(date.today()), '%Y-%m-%d')
#         collection = todocol
#         cursor = collection.find({})
#         for document in cursor:
#             print(document[ObjectId])
#             completed=(document['completed'])
#             scheduled=(document['scheduled'])
#             if(completed!=""):
#                 dictReport["completed"]=document
#             else:
#                 scheduledDate = datetime.strptime(scheduled, '%d/%m/%Y')
#                 if scheduledDate < today:
#                     dictReport["backlog"] = document
#                 else:
#                     dictReport["pending"] = document
#         print(dictReport)
#         response = json.dumps({"success": "true", "status": 200, "message": "Done"})
#         return Response(status=200, response=response)


if __name__ == "__main__":
    app.run(debug=False)

