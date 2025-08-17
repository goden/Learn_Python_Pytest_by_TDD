import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from idv.goden.chapter02.unit06.models import Base

@pytest.fixture(name='session')
def session_fixture() -> Session:
    engine_url = "sqlite://"
    engine = create_engine(engine_url)
    Base.metadata.create_all(engine)

    with sessionmaker(bind=engine)() as session:
        yield session

    Base.metadata.drop_all(bind=engine)
