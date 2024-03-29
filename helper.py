from pymongo import MongoClient


# Summary of a CSV
def summaryCSV(csv_file_path):
    # Print CSV file summary
    print("\nCSV File Summary:")
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header
        num_columns = len(header)
        print("Number of columns:", num_columns)
        print("Columns:")
        for i, column_name in enumerate(header, start=1):
            print(f"{i}. {column_name}")
        num_rows = sum(1 for _ in reader)
        print("\nTotal number of rows:", num_rows)
    print("\n")
    
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

# Give the name of the collection
def defineCollection(db):
    myCollection = input('Input the name of the collection you want to create: ');
    collection = db[myCollection]  
    return collection
 