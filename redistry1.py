import redis
import pymongo
from flask import Flask, Response
import json
import logging
from bson import ObjectId
from todo_handler import TodoHandler


myclient = pymongo.MongoClient('mongodb://localhost:27017/')
tododb = myclient['dbtodo']
todocol = tododb['todotable']

app = Flask(__name__)
redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route("/todoget/<string:id>",methods = ["GET"])
def redis(id):
    # if request.method=='GET':
    data = {"id": id}

    if(redisClient.hexists("redisdict",str(ObjectId(id)))):
        print(redisClient.hget("redisdict", str(ObjectId(id))))
    else:
        output, status_code = todo_handler.get_todo(data)
        redisClient.hset("redisdict", str(ObjectId(id)),output)
        print(redisClient.hget("redisdict", str(ObjectId(id))))

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



if __name__ == "__main__":
    app.run(debug=False)