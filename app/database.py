from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
connection = ""
client = MongoClient("mongodb://localhost:27017/db_name")

print(client.__dict__)

# db = client.theatre_db
db = client.buchi_db

movie_collection = db["pets"]

user_collection = db["customers"]

review_collection = db["adoptions"]




