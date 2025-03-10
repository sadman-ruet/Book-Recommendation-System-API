from pymongo import MongoClient
from pymongo.server_api import ServerApi

def initialize_db(database:str):
    uri = "mongodb+srv://sadmanhasib:sadmanhasib@cluster0.fdf5z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client[database]

