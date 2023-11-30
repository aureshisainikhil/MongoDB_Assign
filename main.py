#! "C:\Users\aures\Envs\test\Scripts\python.exe"
from dotenv import load_dotenv,find_dotenv
from flask import Flask, Request,jsonify, Response
import json
import os
import pprint
from bson import json_util
from pymongo import MongoClient
app = Flask(__name__)
printer = pprint.PrettyPrinter()
# load_dotenv(find_dotenv())
# password = os.getenv("Mongodb_Pswd")
password = "mongodb0463"
connection_string = f"mongodb+srv://sainikhilaureshi97:{password}@cluster0.lqaen7b.mongodb.net/python_db"
try:
    client = MongoClient(connection_string)
    # dbs = client.list_database_names()
    db = client.python_db
    # collections = db.list_collection_names()
    client.server_info()
except:
    print("Error- connect to db")
collection = db.Netflix

movies = collection.find({'id':{'$in':['ts300399','tm84618']}})
# for movie in movies:
# res = json.dumps(movies,indent = 4,default=str)
# res = [{item: data[item] for item in data if item != '_id'} for data in movies]
# res = [{key:movies[key] for key in movies if key != '_id'}]
# print(collection)
for movie in movies:
    pprint.pprint(movie)

# @app.route('/netflix', methods = ['GET'])
# def find_all_movies():
#     movies = collection.find_one({"id":"tm371359"})
#     # movies = collection.find()
#     res = [{key:movies[key] for key in movies if key != '_id'}]  
    
#     return json.dumps(res, cls= DecimalEncoder)

# if __name__=='__main__':
#     app.run(port=5000, debug=True)



