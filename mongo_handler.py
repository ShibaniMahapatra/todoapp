import pymongo
import json

class MongoHandler:
    def __init__(self):
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        self.tododb = 'dbtodo'

    def insert_document(self, collection, document):
        try:
            self.myclient[self.tododb][collection].insert(document)
        except Exception as err:
            raise err

    def get_document(self):
        try:
            taskList = []
            cursor = self.tododb.find({})
            for document in cursor:
                document['_id'] = str(document['_id'])
                taskList.append(document)
            todojson = json.dumps(taskList)
        except Exception as err:
            raise err
