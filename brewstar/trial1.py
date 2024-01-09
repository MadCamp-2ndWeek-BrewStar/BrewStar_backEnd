from pymongo import MongoClient
from flask import Flask, jsonify
import json
from bson import json_util
import datetime

client = MongoClient('127.0.0.1', 27017)

db = client.brewStar
collection = db.users

menu1= {
 "userId" : "3259657340",
 "favorites" : ['659d354761001d4cd66546f1', '659d354761001d4cd66546f3']
}


# L = [menu1]

collection.insert_one(menu1)

# app= Flask(__name__)

# @app.route('/')
# def hello():
#     documents = list(collection.find({"menu": "Iced Caffe Latte"}))

#     filtered_data = []
#     for document in documents:
#         if 'userName' in document:
#             filtered_data.append(document['userName'])

#     return jsonify(filtered_data)