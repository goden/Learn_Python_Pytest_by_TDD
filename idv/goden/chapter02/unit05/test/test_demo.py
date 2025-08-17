import pytest
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from datetime import datetime

from idv.goden.chapter02.unit05.crud.demo import create_user
from idv.goden.chapter02.unit05.crud.demo import create_user_via_mongo
from idv.goden.chapter02.unit05.modes import Base


@pytest.fixture(name='session')
def session_fixture() -> Session:
    engine_url = "sqlite://"
    engine = create_engine(engine_url)
    Base.metadata.create_all(engine)

    with sessionmaker(bind=engine)() as session:
        yield session

    Base.metadata.drop_all(bind=engine)

@pytest.fixture(name='client')
def client_fixture() -> MongoClient:
    with MongoClient() as conn:
        yield conn


def test_create_user(session: Session):
    username = "nick"
    birthday = datetime.now()

    result = create_user(session = session, username = username, birthday = birthday)
    print(result.username)

    assert result.username == username
    assert result.birthday == birthday
    assert result.id is not None


def test_create_user_via_mongo(client: MongoClient):
    username = "nick"
    birthday = datetime.now()

    result = create_user_via_mongo(client=client, username=username, birthday=birthday)
    print(result.get("username"))

    assert result.get("username") == username
    assert result.get("birthday").day == birthday.day
    assert result.get("_id")
