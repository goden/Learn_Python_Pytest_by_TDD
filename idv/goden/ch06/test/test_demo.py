from typing import Any, Generator

import pytest
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from datetime import datetime

from idv.goden.ch06.crud.demo import create_user

def test_create_user(session: Session):
    username = "nick"
    birthday = datetime.now()

    result = create_user(session = session, username = username, birthday = birthday)
    print(result.username)

    assert result.username == username
    assert result.birthday == birthday
    assert result.id is not None
