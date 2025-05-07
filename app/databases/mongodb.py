import os
from dotenv import load_dotenv
from pymongo import MongoClient
from typing import Callable, Coroutine

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

def get_user_collection() -> Callable[[], Coroutine]:
    return db["users"]

def get_article_collection() -> Callable[[], Coroutine]:
    return db["news_articles"]

def get_subscription_collection() -> Callable[[], Coroutine]:
    return db["subscriptions"]

def get_stats_collection() -> Callable[[], Coroutine]:
    return db["statistics"]
