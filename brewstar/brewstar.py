from pymongo import MongoClient
from flask import Flask, jsonify, request
import json
from bson import json_util, ObjectId
from datetime import datetime
from bson.json_util import dumps

app= Flask(__name__)

# 이렇게 함수 밖에 Client가 선언되면, 한 번만 데이터가 보이고 그 다음부터는 Internal Server Error (500)이 뜬다.
# client = MongoClient('localhost', 27017)
# db = client.brewStar
# collection = db.custom_guide

client = MongoClient('localhost', 27017)
db = client.brewStar

@app.route("/myCustom", methods=['GET'])
def myCustom():

    userId = request.args.get('userId')
    if userId:
        # print(userId)
        collection = db.customs
        documents = list(collection.find({"creatornum": userId}))
        print(documents)


        filtered_data = []
        for document in documents:
            custom= []
            itemId= document["_id"]
            str_itemId= str(itemId)
            custom.extend([str_itemId,document['category'],document['name'],document['menu'],document['custom'],document['Description'],document['creator'],document['likes'],document['createdAt']])
            filtered_data.append(custom)
        return jsonify(filtered_data)
    
    else: 
        return "UserId가 없습니다.", 400
    

    
@app.route("/allCustoms", methods=['GET'])
def allCustoms():

    flag = request.args.get('sortFlag')
    print(flag)
   
    collection = db.customs
    documents = list(collection.find())

    filtered_data = []
    for document in documents:
        custom= []
        itemId= document["_id"]
        str_itemId= str(itemId)
        custom.extend([str_itemId, document['category'],document['name'],document['menu'],document['custom'],document['Description'],document['creator'],document['likes'],document['createdAt']])
        filtered_data.append(custom)

    #print(filtered_data)
    #최신순
    if (flag=='Recent'):
        sorted_time_data = sorted(filtered_data, key=lambda x: x[-1], reverse=True)
        return jsonify(sorted_time_data)
    #추천순
    else:
        sorted_likes_data = sorted(filtered_data,key=lambda x: int(x[-2]), reverse=True)
        return jsonify(sorted_likes_data)


 
@app.route("/myFavorite", methods=['GET'])
def myFavorite():

    filtered_data= []
    userId = request.args.get('userId')
    if userId:
        collection =db.users
        info=collection.find_one({"userId": userId})
        # print(info)
        if info: 
            customIds=info.get('favorites', [])
            # print(customIds)
            collection =db.customs
            for customId in customIds:
                # print(customId)
                custom=collection.find_one({'_id': ObjectId(customId)})
                # print(custom)
                if custom:
                    itemId= custom["_id"]
                    str_itemId= str(itemId)
                    c = [str_itemId, custom.get('category'), custom.get('name'), custom.get('menu'), custom.get('custom'), custom.get('Description'), custom.get('creator'), custom.get('likes'), custom.get('createdAt')]
                    filtered_data.append(c)
            return jsonify(filtered_data)
        else:
            return "UserId가 잘못되었습니다.", 400
    else: 
        return "UserId가 없습니다.", 400

@app.route("/test", methods=['GET'])
def test():

    collection = db.customs
    documents = list(collection.find())
    filtered_data = []
    for document in documents:
        custom= []
        custom.extend([document['category'],document['name'],document['menu'],document['custom'],document['Description'],document['creator'],document['likes'],document['createdAt']])
        filtered_data.append(custom)

    return jsonify(filtered_data)
    

@app.route("/addCustom", methods=['POST'])
def addCustom():
    
    collection =db.customs
    
    newCustom = {}
    newCustom["name"] = request.args.get('name')
    newCustom["menu"] = request.args.get('menu')
    newCustom["category"] = request.args.get('category')
    newCustom["custom"] = request.args.get('custom')
    newCustom["Description"] = request.args.get('Description')
    newCustom["creator"] = request.args.get('creator')
    newCustom["creatornum"] = request.args.get('creatornum')
    newCustom["likes"] = "0"
    newCustom["createdAt"] = datetime.now()

    collection.insert_one(newCustom)

@app.route("/editCustom", methods=['POST'])
def editCustom():

    customId = request.args.get('customId')
    
    collection = db.customs

    filter= {'_id': ObjectId(customId)}

    new_values= {
        "$set" : {"name" : request.args.get('name'),
                  "menu" : request.args.get('menu'),
                  "category" : request.args.get('category'),
                  "custom" : request.args.get('custom'),
                  "Description" : request.args.get('Description'),
                  "modifiedAt" : datetime.now()
                  }
    }

    collection.update_one(filter, new_values)


@app.route("/deleteCustom", methods=['POST'])
def deleteCustom():

    customId = request.args.get('customId')

    collection = db.customs

    id = ObjectId(customId)
    collection.delete_one({"_id": id})


@app.route("/likeCustom", methods=['POST'])
def likeCustom():

    userId = request.args.get('userId')
    customId = request.args.get('customId')

    collection = db.users

    filter= {"userId": ObjectId(userId)}
    #print(filter)= {'userId': ObjectId('659d6650ea6c849187d5ced0')}

    info=collection.find_one({"userId": userId})

    #만약 좋아요를 누른적이 있어서 info가 users안에 있다면
    if info:
        customIds=info.get('favorites', [])
        #만약 좋아요를 누르지 않은 것이어서 좋아요를 하는 것이라면
        if (customId not in customIds):
            customIds.append(customId)
            new_values= {
                "$set" : {"favorites" : customIds}
                }
            collection.update_one(filter, new_values)
            #해당 custom 좋아요 수 update
            collection = db.customs
            customFilter= {"_id": ObjectId(customId)}
            custom= collection.find_one({"_id" : ObjectId(customId)})
            newLikes= int(custom["likes"]) + 1
            new_likes= {
                "$set" : {"likes" : str(newLikes) }
            }
            collection.update_one(customFilter, new_likes)

        #만약 좋아요를 누른 것이어서 취소하는 것이면
        elif (customId in customIds):
            customIds.remove(customId)
            new_values= {
                "$set" : {"favorites" : customIds}
                }
            collection.update_one(filter, new_values)
            #해당 custom 좋아요 수 update
            collection = db.customs
            customFilter= {"_id": ObjectId(customId)}
            custom= collection.find_one({"_id" : ObjectId(customId)})
            newLikes= int(custom["likes"]) - 1
            new_likes= {
                "$set" : {"likes" : str(newLikes) }
            }
            collection.update_one(customFilter, new_likes)

    #만약 좋아요를 누른적이 없어서 info가 users안에 없다면
    
    else: 
        newUser = {}
        newUser["userId"] = userId
        newUser["favorites"] = [customId]
        collection.insert_one(newUser)
        #해당 custom 좋아요 수 update
        collection = db.customs
        customFilter= {"_id": ObjectId(customId)}
        custom= collection.find_one({"_id" : ObjectId(customId)})
        newLikes= int(custom["likes"]) - 1
        new_likes= {
            "$set" : {"likes" : str(newLikes) }
        }
        collection.update_one(customFilter, new_likes)


if __name__ ==  "__main__":
    app.run(host='0.0.0.0', port=80)




# client.close()