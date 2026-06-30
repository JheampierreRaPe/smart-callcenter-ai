from pymongo import MongoClient
import redis

from app.core.config import *

mongo_client = MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USER,
    password=MONGO_PASSWORD
)

mongo_db = mongo_client["callcenter"]


redis_db = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)
