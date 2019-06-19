from mongo_handler import MongoHandler

mongo_handler = MongoHandler()

class TodoHandler:

    def create_todo(self, data):
        try:
            mongo_handler.insert_document("todo",data)
            return "Data Inserted", 200
        except Exception as err:
            return "data not inserted",400

    def get_todo(self):
        try:
            mongo_handler.get_document("todo")
            return "Data displayed", 200
        except Exception as err:
            return "data not displayed",400