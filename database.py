from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()

def initialize_db(database:str):
    try:
        uri = os.getenv("MONGODB_URL")
    except:
        uri = "mongodb://localhost:27017/"
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client[database]

