from sqlalchemy.orm import Session
from idv.goden.ch05.modes.demo import DemoUser
from datetime import datetime

from pymongo.mongo_client import MongoClient

def create_user(session:Session, username:str, birthday:datetime):
    user = DemoUser(username = username, birthday = birthday)
    session.add(user)
    session.commit()
    session.refresh(user)

    return user

def create_user_via_mongo(client:MongoClient, username:str, birthday:datetime):
    inserted_id = client["demo"]["user"].insert_one(
        {"username": username, "birthday": birthday}
    ).inserted_id
    return client["demo"]["user"].find_one({"_id": inserted_id})
