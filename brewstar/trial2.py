from pymongo import MongoClient
from flask import Flask, jsonify, render_template
import json
from bson import json_util
import datetime

app= Flask(__name__)

# @app.route("/", methods=['GET'])
# def hello():
#     return "Hello, World!"

@app.route("/frappuccino", methods=['GET'])
def mongo():
    client = MongoClient('localhost', 27017)

    db = client.brewStar
    collection = db.custom_guide

    # menu1= {
    # "menu": "Iced Caffe Latte",
    # "desc": "u can customize~"
    # }
    # menu2= {
    # "menu": "Iced Caffe Americano",
    # "desc": "u can customize~"
    # }

    # L = [menu1,menu2]

    # collection.insert_many(L)

    # results = collection.find()

    documents = list(collection.find({"menu": "Iced Caffe Latte"}))

    filtered_data = []
    for document in documents:
        if 'desc' in document:
            filtered_data.append(document['desc'])

    client.close()

    return jsonify(filtered_data)

if __name__ ==  "__main__":
    app.run(host='0.0.0.0', port=80)