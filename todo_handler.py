from mongo_handler import MongoHandler
from bson import ObjectId

mongo_handler = MongoHandler()


class TodoHandler:

    def create_todo(self, data):
        try:
            mongo_handler.insert_document("todotable", data)
            return "Data Inserted", 200
        except Exception as err:
            return "data not inserted", 400

    def get_todo(self,data):
        try:
            if data==None:
                query={}
            else:
                query = {"_id":ObjectId(data["id"])}

            outputData = mongo_handler.get_document(query)
            # print(outputData)
            return outputData, 200
        except Exception as err:
            return "data not displayed", 400

    def delete_todo(self, data):
        try:
            if data==None:
                query = {}
            else:
                query = {"_id":ObjectId(data["id"])}

            mongo_handler.delete_document(query)
            return "deleted", 200
        except Exception as err:
            return "data not deleted", 400

    def get_todo_one(self,id):
        try:
            mongo_handler.get_document_one(id)
            return "document displayed one", 200
        except Exception as err:
            return "data not displayed", 400

    def delete_todo_one(self):
        try:
            mongo_handler.delete_document_one()
            return "document deleted", 200
        except Exception as err:
            return "data not deleted", 400
