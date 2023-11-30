In this assignment, you will learn and implement CRUD(Create, Read, Update, Delete). These are the basic APIs to perform at most functions on web applications. You will develop the backend web framework using Python Flask connect to MongoDB (https://www.mongodb.com). There are some videos on Blackboard about Flask framework and MongoDB that you can study before starting this assignment. To test the backend web framework, you can use API platforms such as Postman API Platform(https://www.postman.com) or Swagger UI such as FastAPI(https://fastapi.tiangolo.com/).
The CSV file(netflix.csv-Movie and Show on Netflix) is provided in this assignment with the column names including: 
age_certification
description
genres
id
imdb_score
production_countries
release_year
runtime
title
type

First, the instructor will guide you how to generate MongoDB Database and collections using MongoDB Compass or Atlas. You will import this csv file to collection netflix on MongoDB database in JSON format. 

This is a sample on python file:
The MongoDB Configuration: (local database-MongoDB Compass).
Host = ‘localhost’
Port = 27017
Database name = database
Collection name = netflix 
… 
try:
    mongo = pymongo.MongoClient(
        host = 'localhost',
        port = 27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.database
    mongo.server_info() #trigger exception if cannot connect to db
except:
    print("Error -connect to db")

In xxxx.py file, you must perform the following main functions: 
1.	Insert the new movie and show. 
@app.route('/netflix', methods=['POST'])

2.	Update the movie and show information using title. (By update only id, title, description, runtime, and imdb_score).
@app.route('/netflix/<string:fname>', methods=['PATCH'])

3.	Delete the movie and show information using title.
@app.route('/netflix/<string:fname>', methods=['DELETE'])

4.	Retrieve all the movies and shows in database.
@app.route('/netflix', methods=['GET'])



5.	Display the movie and show’s detail using title.
@app.route('/netflix/<string:fname>', methods=['GET'])
