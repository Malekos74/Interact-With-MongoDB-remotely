from pymongo import MongoClient
from helper import connectMongoDB, defineDB, defineCollection

# Extracts values out of the querried value
def extractValues(list):
    return [list[0]['P'], list[0]['Q'], list[0]['P_ref']]

# Prints a list with the number of objects printed
def printList(list):
    print("\n")
    for x in list:
        print(x)
    print("\nPrinted ", len(list), " Objects.")

# Processes the result of a querry
def processResult(result):
    if result is not None:
        # Prints the querried values on STDOUT
        printList(result)
        
        # Initialize all needed variables for later use
        [P, Q, P_ref] = extractValues(result)  
        # print(P)
        # print(Q)
        # print(P_ref)
    else:
        print("Rerun the code and input an existing timestep.")
                
    # printAllTimesteps(db, collection)
    
# Querries from the specified DB and collection based on an inputted timestep. Returns a list of the form:
# [documents, P, Q, P_ref, timestep] with documents being a list of dictionaries. Each dictionary represents an object
# that exist in that DB and collection and has a Time [s] value of timestep. 
def querry(db , collection, timestep = -1):  
    # Documentation on how to build complex querries: https://www.w3schools.com/python/python_mongodb_query.asp
    
    # Access the current database
    current_db_name = db.name
    print("\nCurrent database:", current_db_name)
    # Correctly print the current collection
    print("Current collection:", collection, "\n")
    
    # Fetch all documents from the collection (Empty list if no row exists for the specified timestep)
    documents = list(collection.find({'Time [s]': timestep}))
    
    if len(documents) == 0:
        print("No row exists with the specified timestep: ", timestep)
        # printList(list(collection.find()))
        return None
    
    return documents

# Prints all timesteps of the given collection in the given DB that are not NA
def printAllTimesteps(db , collection):
     # Access the current database
    current_db_name = db.name
    print("\nCurrent database:", current_db_name)
    # Correctly print the current collection
    print("Current collection:", collection, "\n")
    
    # Fetch all documents from the collection (Empty list if no row exists for the specified timestep)
    documents = list(collection.find())
    
    # Assuming documents is a list of dictionaries
    time_values = [doc.get('Time [s]', None) for doc in documents]
    # Filtering out None values if any
    time_values = [value for value in time_values if value is not None]
    # Sort time_values
    time_values.sort()

    # Printing the list of time values
    print(time_values)
    
def querryFromMongoDB(client = None):
    if client == None:
        client = connectMongoDB()
    db = defineDB(client)
    collection = defineCollection(db)
    
    # Specify a Timestep. None if the conversion fails.
    try:
        timestep = float(input("Input the wanted timestep: "))
    except ValueError:
        timestep = None
    
    result = querry(db, collection, timestep)
    processResult(result)
    
    return result

if __name__ == '__main__':
    querryFromMongoDB()
    