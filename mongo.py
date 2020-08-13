import pymongo
import os


MONGODB_URI = "mongodb://root:RootUser@myfirstcluster-shard-00-00.zhfps.mongodb.net:27017,myfirstcluster-shard-00-01.zhfps.mongodb.net:27017,myfirstcluster-shard-00-02.zhfps.mongodb.net:27017/myTestDB?ssl=true&replicaSet=atlas-z7d5ni-shard-0&authSource=admin&retryWrites=true&w=majority"
DBS_NAME = "myTestDB"
COLLECTION_NAME = "breakfast"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

new_doc = [{'category': 'veg_menu', 'name': 'sambar rice', 'quantity': '170 grams', 'price': '3 dollars', 'calories': '300'}, {'category': 'veg_menu', 'name': 'curd rice', 'quantity': '170 grams', 'price': '3 dollars', 'calories': '200'}, {'category': 'veg_menu', 'name': 'coconut rice', 'quantity': '170 grams', 'price': '3 dollars', 'calories': '300'}, {'category': 'veg_menu', 'name': 'veg pulao', 'quantity': '170 grams', 'price': '3 dollars', 'calories': '300'},{'category': 'veg_menu', 'name': 'tomato rice', 'quantity': '170 grams', 'price': '3 dollars', 'calories': '300'}, {'category': 'veg_menu', 'name': 'pulihora', 'quantity': '170 grams', 'price': '3 dollars', 'calories': '300'}]
coll.insert_many(new_doc)

#coll.update_many({'category':'non_veg_menu'},{'$set':{'price':'6 dollars'}})

documents = coll.find()

for doc in documents:
    print(doc)