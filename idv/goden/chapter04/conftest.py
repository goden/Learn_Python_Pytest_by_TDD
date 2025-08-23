from typing import Any, Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from idv.goden.chapter04.models import Base

@pytest.fixture(name="sqlite_session")
def sqlite_session_fixture() -> Generator[Any, Any, None]:
    engine_url = "sqlite://"
    engine = create_engine(engine_url)

    Base.metadata.create_all(engine)

    with sessionmaker(bind=engine) as session:
        yield session

    Base.metadata.drop_all(engine)