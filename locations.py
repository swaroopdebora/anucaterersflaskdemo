import pymongo
import os

MONGODB_URI = "mongodb://root:RootUser@myfirstcluster-shard-00-00.zhfps.mongodb.net:27017,myfirstcluster-shard-00-01.zhfps.mongodb.net:27017,myfirstcluster-shard-00-02.zhfps.mongodb.net:27017/myTestDB?ssl=true&replicaSet=atlas-z7d5ni-shard-0&authSource=admin&retryWrites=true&w=majority"
DBS_NAME = "myTestDB"
COLLECTION_NAME = "locations"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def get_location():
    print("Hi")
    location = input("Enter location> ")
    try:
        doc = coll.find_one({'name': location.lower()})
    except:
        print("Error accessing the database")
    
    if not doc:
        print("")
        print("Error! No locations found.")
    
    return doc

def show_menu():
    print("")
    print("1. Add a new location")
    print("2. Find a locations")
    print("3. Edit a location timimgs")
    print("4. Delete a location")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def get_location():
    print("")
    print("")
    location = input("Enter location> ")
    try:
        doc = coll.find_one({'location': location.lower()})
    except:
        print("Error accessing the database")
    
    if not doc:
        print("")
        print("Error! No results found.")
    
    return doc

def show_location():
    print("")
    print("1. Add a new locations")
    print("2. Find an locations by name")
    print("3. Edit a locations timimgs")
    print("4. Delete a locations")
    print("5. Exit")

    option = input("Enter option: ")
    return option

def add_location():
    print("")
    location = input("Enter location> ")
    timings = input("Enter timings > ")
    dineavailable = input("Enter dine available: Y/N > ")
    

    new_doc = {'location': location.lower(), 'timings': timings.lower(), 'dineavailable': dineavailable.lower() }
    
    try:
        coll.insert(new_doc)
        print("")
        print("location inserted")
    except:
        print("Error accessing the database")


def find_location():
    doc = get_location()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def edit_location():
    doc = get_location()
    if doc:
        
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v
        
        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("location updated")
        except:
            print("Error accessing the database")


def delete_location():

    doc = get_location()

    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
        
        print("")
        confirmation = input("Sure you want to delete this location ?\nY or N > ")
        print("")

        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("location deleted!")
            except:
                print("Document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_location()
        elif option == "2":
            find_location()
        elif option == "3":
            edit_location()
        elif option == "4":
            delete_location()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()