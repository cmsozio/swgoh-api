import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.swgoh

def check_document(collection, doc_id):
    col = db[collection]
    document = col.find_one(doc_id)
    if document == None:
        return {"message": "error"} 
    return {"message": "success"}

#Recieve json data from api, and create database entry for that given allycode
def create_documents(collection, data):
    allycode = data["allyCode"]
    doc_id = {"_id": allycode}
    message = check_document(collection, doc_id)
    if message["message"] == "error":
        data.update({"_id": allycode}) #create a primary key for the document
        col = db[collection]
        doc_id = col.insert_one(data).inserted_id
        return doc_id
    else:
        return update_documents(collection, data)

#Recieve json data from api, and update the database entry for that given allycode
def update_documents(collection, data):
    allycode = data["allyCode"]
    doc_id = {"_id": allycode}
    message = check_document(collection, doc_id)
    if message["message"] == "error":
        return create_documents(collection, data)
    else:
        col = db[collection]
        for item in data:
            update = {"$set": {item: data[item]}} #mongo only updates with '$' operators
            result = col.update_one(doc_id, update)
        return {"matched": result.matched_count, "modified": result.modified_count}

def query_documents(collection, query):
    col = db[collection]
    doc_id = {"_id": query["_id"]}
    document = col.find(doc_id, query)
    return document


#Testing
"""
f = open("json/player/413422952-player.json")
json_data = json.loads(f.read())
print(update_documents("players", json_data))
"""
#collection.find_one_and_update(filter, update) update_one(filter, update)