"""
    Python program that helps you to import a .csv file into a fresh or pre-existing Mongo DB
        
    INPUT:
        - Mongo Client connection string (Default: mongodb://localhost:27017)
        - Database name
        - Collection name
        - csv file path
        - number of rows to import (Default: All rows)
    OUTPUT:
        - Edits/ Creates a database with the specified name, creates a collection with the specified name
          and imports the specified number of rows of the csv file
    
    NB:
        - If the program times out at any point, please check your inputs and try again.
        
"""
import csv
from pymongo import MongoClient
from helper import connectMongoDB, defineDB, defineCollection

# Read CSV file and insert into MongoDB
# C:\Users\malek\Desktop\Malek\Studium\B.Sc Informatik (TUM)\Semester 3\EDGE\EDL\task_43\winddata
def importCSV(collection):
    csv_file_path = input("Enter the full path to the CSV file without the .csv extension (Or just the file name if it is in the same DIR): ")
    csv_file_path += '.csv'
    nrows = input("Input how many rows you want to import (Press ENTER to import all rows): ")
    nrows = int(nrows) if nrows else -1 

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        row_count = 0
        for row in reader:
            collection.insert_one(row)
            row_count += 1
            if row_count % 1024 == 0:
                print("Import in progress... Rows inserted:", row_count)
            if row_count == nrows :
                break
                
    print("Import completed! Total rows inserted:", row_count)

def importToMongoDB(client = None):
    if client == None:
        client = connectMongoDB()
    db = defineDB(client)
    collection = defineCollection(db)
    importCSV(collection)
    
if __name__ == '__main__':
    importToMongoDB()


