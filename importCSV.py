import csv
from pymongo import MongoClient
from helper import connectMongoDB, defineDB, defineCollection, summaryCSV
  
# Read CSV file and insert into MongoDB
# C:\Users\malek\Desktop\Malek\Studium\B.Sc Informatik (TUM)\Semester 3\EDGE\EDL\task_43\winddata
def importCSV(collection):
    csv_file_path = input("Enter the full path to the CSV file without the .csv extension (Or just the file name if it is in the same DIR): ")
    csv_file_path += '.csv'
    
    # Print a summary of the CSV file
    summaryCSV(csv_file_path)
    
    columns_to_import = input("Input column numbers you want to import (separated by commas, e.g., 1,2,3): ")
    columns_to_import = [int(column.strip()) - 1 for column in columns_to_import.split(",")]  # Adjust to 0-based index
    
    lower = input("Input lower interval limit (inclusive) of rows you want to import (Press ENTER to import all rows): ")
    lower = int(lower) if lower else -1 
    
    higher = input("Input higher interval limit (inclusive) of rows you want to import (Press ENTER to import all rows): ")
    higher = int(higher) if higher else -1 

    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Get header
        selected_columns = [header[i] for i in columns_to_import]
        
        row_count = 0
        for row in reader:
            row_count += 1
            if (lower == -1 or row_count >= lower) and (higher == -1 or row_count <= higher):
                filtered_row = {header[i]: row[i] for i in columns_to_import}
                collection.insert_one(filtered_row)
                if row_count % 1024 == 0:
                    print("Import in progress... Rows inserted:", row_count)
                if row_count == higher:  # Stop if reached the higher limit
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
