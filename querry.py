from pymongo import MongoClient
from helper import connectMongoDB, defineDB, defineCollection, summaryCSV

# Prints the querried documents in a readable way.
def printDocuments(documents, field, value):
    # Print each document in a nice format
    print(f"Documents where {field} is '{value}':")
    for idx, document in enumerate(documents, 1):
        print(f"Document {idx}:")
        for key, val in document.items():
            print(f"\t{key}: {val}")
        print()  # Add an empty line between documents
        
# Prints a list with the number of objects printed
def printList(list):
    print("\n")
    for x in list:
        print(x)
    print("\nPrinted ", len(list), " Objects.")

# Query one object out of the collection so that the user knows how it looks like
def queryOne(db , collection):  
    # Documentation on how to build complex querries: https://www.w3schools.com/python/python_mongodb_query.asp
    
    # Access the current database
    current_db_name = db.name
    print("\nCurrent database:", current_db_name)
    # Correctly print the current collection
    print("Current collection:", collection, "\n")
    
    # Fetch all documents from the collection (Empty list if no row exists for the specified timestep)
    document = list(collection.find_one())
    
    print(document)
    
    return document 
   
# Querries from the specified DB and collection based on an inputted timestep. Returns a list of the form:
# [documents, P, Q, P_ref, timestep] with documents being a list of dictionaries. Each dictionary represents an object
# that exist in that DB and collection and has a Time [s] value of timestep. 
def query(db, collection, field, value):
    # Access the current database
    current_db_name = db.name
    print("\nCurrent database:", current_db_name)
    # Correctly print the current collection
    print("Current collection:", collection, "\n")
    
    # Fetch all documents from the collection based on the provided field and value
    documents = list(collection.find({field: value}))
    
    if len(documents) == 0:
        print(f"No documents found where {field} is '{value}'")
        return None
    else:    
        printDocuments(documents, field, value)
    
    return documents

    
def queryFromMongoDB(client = None):
    if client == None:
        client = connectMongoDB()
    db = defineDB(client)
    collection = defineCollection(db)
    
    # query one object and print it for the user to know what the collection looks like
    result = queryOne(db, collection)
    
    # Ask the user for the field and value they want to query
    field = input("Enter the field you want to query: ")
    value = input(f"Enter the value for the field '{field}': ")
    
    # Check if the value is numerical (if it is, it will get converted and used since the value saved in the db would also be numerical)
    try:
        value = int(value)  # Try converting to integer first
    except ValueError:
        try:
            value = float(value)  # Try converting to float if int conversion fails
        except ValueError:
            pass  # If conversion to int and float fails, keep it as string
    
    # Query with the provided field and value
    result = query(db, collection, field, value)
    
    return result

if __name__ == '__main__':
    queryFromMongoDB()
    