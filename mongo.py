import pymongo
import os


MONGODB_URI = "mongodb://root:RootUser@myfirstcluster-shard-00-00.zhfps.mongodb.net:27017,myfirstcluster-shard-00-01.zhfps.mongodb.net:27017,myfirstcluster-shard-00-02.zhfps.mongodb.net:27017/myTestDB?ssl=true&replicaSet=atlas-z7d5ni-shard-0&authSource=admin&retryWrites=true&w=majority"
DBS_NAME = "myTestDB"
COLLECTION_NAME1 = "breakfast"
COLLECTION_NAME2 = "locations"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)
coll1 = conn[DBS_NAME][COLLECTION_NAME1]

coll2 = conn[DBS_NAME][COLLECTION_NAME2]


def find_menu(category):
    docs = coll1.find({'category': category})
    x = []
    for i in docs:
        x.append(i)
    for item in x:
        print(item["name"]+" -  price is "+item["price"]+" and calories is "+item["calories"])


#find_menu("sweets")

def find_locations():
    docs = coll2.find()
    x=[]
    for i in docs:
        x.append(i)
    for item in x:
        print(item["location"]+" - timings are from "+item["timings"]+" , Dining Available ?- "+item["dineavailable"])


#find_locations()

def update_locations():
    listoflocations1 = ["Brampton","Missasaga","Toronto"]
    listoflocations2 = ["Brampton","Missasaga","Toronto","Hamilton","North York"]
    docs = coll1.update_many({'category':'veg_menu'},{'$set':{'location':listoflocations2}})
    print("hi")
    

update_locations()
