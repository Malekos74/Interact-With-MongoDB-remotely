# Interact with mongoDB remotely

## connection.py
### Description:
This script is the main script to be run.
### Input:
- Input 1 if you want to import a CSV to the mongoDB, 0 to querry.
### Output:
- Based on the input, the respective script will be run to either import a csv to a mongoDB or to querry out of a mongoDB.

## helper.py
### Description:
This script contains some helpful functions used to setup the connection to a mongoDB instance.
The functions are: connectMongoDB, defineDB, defineCollection
### Input:
- No input
### Output:
- No output

## querry.py
### Description:
querryFromMongoDB(client) is the main function here.
### Input:
- Client (if the there is no passed value)
- DB name
- Collection name
- Timestep
### Output:
- Outputs the row that matches with the wanted timestep

## importCSV.py
### Description:
importToMongoDB(client) ist the main function here.
### Input:
- Client (if the there is no passed value)
- DB name
- Collection name
- Path of the csv file to import.
### Output:
- Imports the wanted csv to the specified mongoDB 
