import pymongo
import os


MONGODB_URI = "mongodb://root:RootUser@myfirstcluster-shard-00-00.zhfps.mongodb.net:27017,myfirstcluster-shard-00-01.zhfps.mongodb.net:27017,myfirstcluster-shard-00-02.zhfps.mongodb.net:27017/task_manager?ssl=true&replicaSet=atlas-z7d5ni-shard-0&authSource=admin&retryWrites=true&w=majority"
DBS_NAME = "task_manager"
COLLECTION_NAME1 = "task"
COLLECTION_NAME2 = "categories"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)
coll1 = conn[DBS_NAME][COLLECTION_NAME1]

coll2 = conn[DBS_NAME][COLLECTION_NAME2]

def add_task():
    new_doc = [ {"category_name":"cooking"},{"category_name":"cleaning"},{"category_name":"shoping"},{"category_name":"book_keeping"}]
    coll2.insert_many(new_doc)


def add_category():
    new_doc = [ {"task_name":"chopping Vegetables","category_name":"cooking","task_description":"finely chopping all the vegetables needed for salads and cooking","due_time":"7am","frequency":"daily"},{"task_name":"chopping Vegetables","category_name":"cooking","task_description":"finely chopping all the vegetables needed for salads and cooking","due_time":"7am","frequency":"daily"},{"task_name":"cleaning the common area","category_name":"cleaning","task_description":"cleaning the tables and floor","due_time":"9pm","frequency":"daily"},{"task_name":"Accounts for the day","category_name":"book_keeping","task_description":"finalize the trail balance for the day","due_time":"10pm","frequency":"daily"}]
    coll1.insert_many(new_doc)

add_task()

add_category()