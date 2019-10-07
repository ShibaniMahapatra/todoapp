from mongo_handler import MongoHandler
from bson import ObjectId

mongo_handler = MongoHandler()


class TodoHandler:
    def register_todo(self, data):
        try:
            print(type(data))
            print(data)
            if 'name' in data.keys() \
                    and 'age' in data.keys() and 'address' in data.keys() and 'sex' in data.keys() \
                    and 'emailId' in data.keys() and 'contact' in data.keys():
                print("present2")
                mongo_handler.insert_register_document("todotable", data)
                return "Data Inserted", 200
            else:
                return "data not inserted", 400
        except Exception as err:
            return "data not inserted", 400

    def create_todo(self, data):
        try:
            print(type(data))
            print(data)
            if 'created' in data.keys() \
                    and 'scheduled' in data.keys() and 'completed' in data.keys() and 'description' in data.keys() \
                    and 'title' in data.keys() and 'lastupdated' in data.keys():
                print("present2")
                mongo_handler.insert_col_document("todotable", data)
                return "Data Inserted", 200
            else:
                return "data not inserted", 400
        except Exception as err:
            return "data not inserted", 400

    def get_todo(self, data):
        try:
            if data == None:
                query = {}
            else:
                query = {"_id": ObjectId(data["id"])}

            outputData = mongo_handler.get_document(query)
            return outputData, 200
        except Exception as err:
            return "data not displayed", 400

    def delete_todo(self, data):
        try:
            if data == None:
                query = {}
            else:
                query = {"_id": ObjectId(data["id"])}

            mongo_handler.delete_document(query)
            return "deleted", 200
        except Exception as err:
            return "data not deleted", 400

    # def get_todo_one(self,id):
    #     try:
    #         mongo_handler.get_document_one(id)
    #         return "document displayed one", 200
    #     except Exception as err:
    #         return "data not displayed", 400
    #
    # def delete_todo_one(self):
    #     try:
    #         mongo_handler.delete_document_one()
    #         return "document deleted", 200
    #     except Exception as err:
    #         return "data not deleted", 400
