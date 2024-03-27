"""
    Python program that helps you connect to a specified mongoDB on a remote server.
        
    INPUT:
        - 1 or 0 based on the functionality needed
        - Database name 
        - Collection name 
        - Timestep (if querrying / input through STDIN)
        - Path of the CSV (if importing)
        - Number of rows to import (if importing)
    OUTPUT:
        - All objects that have the timestep inputted (if querrying)
        - The number of rows imported (if importing)
        
    
    NB:
        - You need to be connected to the Uni network for the SSH connection to work (Or use eduVPN)
        - Input float should be with a '.' and not a ','
        - If the following error message appears when querrying: "No row exists with the specified timestep None",
          then the conversion of the input into float failed. Please check the timestep and try again.
        - If the program times out at any point, please try again.
        
[Malek Miled] 27.03.2024
"""
from importCSV import importToMongoDB
from querry import querryFromMongoDB
from pymongo import MongoClient
from sshtunnel import SSHTunnelForwarder

# SSH tunnel parameters (Can be changed accordingly)
SSH_HOST = 'YOUR HOST'
SSH_USER = 'YOUR USERNAME'
SSH_PASSWORD = 'YOUR PASSWORD'
SSH_PORT =  22  # Default SSH port

# MongoDB parameters (Can be changed accordingly)
MONGO_HOST = '127.0.0.1'  # This points to localhost because MongoDB will be accessed through the SSH tunnel
MONGO_PORT =  27017
    
# Extracting the values takes into consideration that the result of the querry
# will always be a list of length 1 since time values are unique
if __name__ == '__main__':
    try:
        # Connect to MongoDB through the SSH tunnel
        with SSHTunnelForwarder(
            (SSH_HOST, SSH_PORT),   
            ssh_username = SSH_USER,
            ssh_password = SSH_PASSWORD,
            remote_bind_address = ('127.0.0.1', MONGO_PORT)
        ) as tunnel:

            client = MongoClient(MONGO_HOST, tunnel.local_bind_port)
            
            if int(input("Input 1 if you want to import a CSV to the mongoDB, 0 to querry: ")) == 1:
                importToMongoDB(client)
            else:
                result = querryFromMongoDB(client)
                             
    except Exception as e:
        print("An error occurred:", e)
