#! "C:\Users\aures\Envs\test\Scripts\python.exe"
from dotenv import load_dotenv,find_dotenv
import os
from flask import Flask, jsonify, request, Response
from bson import ObjectId
from pymongo import MongoClient

load_dotenv(find_dotenv())
password = os.getenv("Mongodb_Pswd")
connection_string = f"mongodb+srv://sainikhilaureshi97:{password}@cluster0.lqaen7b.mongodb.net/python_db"
try:
    client = MongoClient(connection_string)
    db = client.python_db
    client.server_info()
except:
    print("Error- connect to db")
    
collection = db.Netflix
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to Netflix "

@app.route("/netflix/between/<string:btwn>",methods = ['GET'])
def betwn(btwn):
    movies = collection.find({'title':{'$regex':'ter'}}).sort("runtime",-1)
    output = [{item: data[item] for item in data if item in ['id','title','runtime']} for data in movies]
    return jsonify(output)                

@app.route("/netflix/", methods=["GET"])
def netflixMoviesList():
    try:
        list_of_all_movies = collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in list_of_all_movies]
        return jsonify(output)
    except Exception as e:
        response = Response("Search Records Error!!",status=500,mimetype='application/json')
        return response

@app.route('/netflix/', methods=['POST'])
def insertNewFilm():
    try:
      data = request.get_json()
    #   print(data['id'])
      movie = collection.find_one({'id':data['id']})
      if movie == None:
        dbResponse = collection.insert_one(data)
        response = Response("New Movie added",status=201,mimetype='application/json')
        return response
      else:
          return Response("Movie Already Exists!!")
    except Exception as e:
        response = Response("Failed to insert New Movie!!",status=500,mimetype='application/json')
        return response

@app.route('/netflix/<string:title>', methods=['DELETE'])
def deleteMovie(title):
   try:
      res = collection.delete_one({'title': title})
      if res.deleted_count!= 0:
        return Response("Movie Deleted successfully!",status=201,mimetype='application/json')
      else:
          return f"{res.deleted_count} movie records deleted"
   except Exception as e:
      response = Response('Delete Movie error!!', status=500, mimetype='application/json')
      return response

@app.route('/netflix/<string:title>', methods=['PATCH'])
def updateMovieDetails(title):
    try:
        data = request.get_json()
        dbResponse = collection.update_one({'title': title}, {'$set': data})
        return Response("Movie updated Successfully",status=201,mimetype='application/json')
    except Exception as e:
        response = Response('Failed to Update Movie Details!!', status=500, mimetype='application/json')
        return response

@app.route('/netflix/<title>')  
def getMovieByTitle(title):
    try:
        movies = collection.find_one({'title': title})
        output = [{item: movies[item] for item in movies if item != '_id'}]
        return jsonify(output)
    except Exception as e:
        response = Response("Record Not Found!!")
        return response, 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)