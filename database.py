from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def initialize_db(database: str):
    # Get MongoDB URI from environment, fallback to localhost if not found
    uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

    try:
        # Connect to MongoDB
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')  # Test the connection
        print(f"✅ Connected to MongoDB database: {database}")
        return client[database]
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        return None
