from pymongo import MongoClient
from flask import Flask, jsonify
import json
from bson import json_util
import datetime

client = MongoClient('127.0.0.1', 27017)

db = client.brewStar
collection = db.customs

menu1= {
  "name" : "레몬 아샷추",
"menu": "Iced Caffe Americano",
"category": "Coffee",
"custom": "샷2+레몬시럽+복숭아티백",
"Description": "새콤달콤한 맛에 씁쓸한 커피! 오묘하게 잠 깨고 싶으면 추천합니다~",
"creator": "송한이",
"creatornum": "3259210919",
"likes": "101",
"createdAt" : datetime.datetime.now()
}


# L = [menu1,]

collection.insert_one(menu1)
# collection.insert_many(L)


# app= Flask(__name__)

# @app.route('/')
# def hello():
#     documents = list(collection.find({"menu": "Iced Caffe Latte"}))

#     filtered_data = []
#     for document in documents:
#         if 'userName' in document:
#             filtered_data.append(document['userName'])

#     return jsonify(filtered_data)