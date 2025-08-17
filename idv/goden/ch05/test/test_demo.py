from typing import Any, Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from datetime import datetime

from idv.goden.ch05.crud.demo import create_user
from idv.goden.ch05.modes import Base


@pytest.fixture(name='session')
def session_fixture() -> Generator[Session, Any, None]:
    engine_url = "sqlite://"
    engine = create_engine(engine_url)
    Base.metadata.create_all(engine)

    with sessionmaker(bind=engine)() as session:
        yield session

    Base.metadata.drop_all(bind=engine)

def test_create_user(session: Session):
    username = "nick"
    birthday = datetime.now()

    result = create_user(session = session, username = username, birthday = birthday)

    assert result.username == username
    assert result.birthday == birthday
    assert result.id is not None
