from pymongo import MongoClient

# Connect to MongoDB using the inputted connection string
def connectMongoDB():
    connectionString = input("Input the connection string to the wanted Mongo Client (Press ENTER for the default localhost): ")
    defaultConnectionString = "mongodb://localhost:27017"    
    if connectionString == '':
        client = MongoClient(defaultConnectionString)
    else:
        client = MongoClient(connectionString)
        
    return client

# Give the name of the database (Can be a preexisting one)
def defineDB(client):
    myDB = input('Input the name of the Database you want to use: ')
    db = client[myDB]
    return db

# Give the name of the collection (Cannot be a preexisting one to avoid issues with having a collision between an old _id and a new one)
def defineCollection(db):
    while True:
        myCollection = input('Input the name of the collection you want to create: ');
        list_of_collections = db.list_collection_names()
    
        if myCollection in list_of_collections :
            print('This collection already exists!')
        else:
            collection = db[myCollection]
            break
        
    return collection
 