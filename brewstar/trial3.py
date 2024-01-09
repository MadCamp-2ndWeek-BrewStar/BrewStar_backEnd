from pymongo import MongoClient
from flask import Flask, jsonify, render_template
import json
from bson import json_util
import datetime

app= Flask(__name__)

# 이렇게 함수 밖에 Client가 선언되면, 한 번만 데이터가 보이고 그 다음부터는 Internal Server Error (500)이 뜬다.
# client = MongoClient('localhost', 27017)
# db = client.brewStar
# collection = db.custom_guide

client = MongoClient('localhost', 27017)

@app.route("/frappuccino", methods=['GET'])
def mongo():
    db = client.brewStar
    collection = db.custom_guide

    documents = list(collection.find({"category": "Frappuccino"}))

    filtered_data = []
    for document in documents:
        if 'menu' in document:
            filtered_data.append(document['menu'])

    client.close()

    return jsonify(filtered_data)
    adsadsasdsd

if __name__ ==  "__main__":
    app.run(host='0.0.0.0', port=80)