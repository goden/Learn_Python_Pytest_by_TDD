from sqlalchemy.orm import Session
from idv.goden.ch05.modes.demo import DemoUser
from datetime import datetime

def create_user(session:Session, username:str, birthday:datetime):
    user = DemoUser(username = username, birthday = birthday)
    session.add(user)
    session.commit()
    session.refresh(user)

    return user
