import pymongo
import json
from bson import ObjectId


class MongoHandler:
    def __init__(self):
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        self.tododb = self.myclient['dbtodo']
        self.todocol = self.tododb['todotable']
        self.registercol=self.tododb['registertable']

    def insert_register_document(self, collection, document):
        try:
            # self.myclient[self.tododb][collection].insert(document)
            self.registercol.insert(document)
        except Exception as err:
            raise err

    def insert_col_document(self, collection, document):
        try:
            # self.myclient[self.tododb][collection].insert(document)
            self.todocol.insert(document)
        except Exception as err:
            raise err

    def get_document(self,query):
        try:
            taskList = []
            cursor = self.todocol.find(query)
            for document in cursor:
                document['_id'] = str(document['_id'])
                taskList.append(document)
            taskJson = json.dumps(taskList)
            # print(taskJson)
            return taskJson
        except Exception as err:
            raise err

    def delete_document(self, query):
        try:
            self.todocol.delete_many(query)
            # cursor = todocol.find({})
            # for document in cursor:
            #     print(document)
            # return "DeleteAllDone"
        except Exception as err:
            raise err

    def delete_document_one(self):
        try:
            self.todocol.delete_one({"_id": ObjectId("5d154ac4211df0be95238ed5")})
            # cursor = self.todocol.find({})
            # for document in cursor:
            #     print(document)
        except Exception as err:
            raise err

    def get_document_one(self,id):
        try:
            for i in self.todocol.find({"_id": ObjectId(id)}):
                print(i)
        except Exception as err:
            raise err