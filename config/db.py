from pymongo import MongoClient
db_connection = MongoClient("mongodb://localhost:27017")
db = db_connection.fastApi
collection = db["API_REST"]