from pymongo import MongoClient

db_connection = MongoClient("mongodb://localhost:27017")
db = db_connection.king_tide
collection = db["user"]
collection_files = db["files"]
