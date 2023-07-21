from pymongo import MongoClient
import os

from dotenv import load_dotenv
load_dotenv()


MONGODB = os.getenv("MONGODB")
print(MONGODB)
db_connection = MongoClient(MONGODB)
db = db_connection.king_tide
collection = db["user"]
collection_files = db["files"]
