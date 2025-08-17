from sqlalchemy.orm import Session
from datetime import datetime

from idv.goden.chapter02.unit06.crud.demo import create_user

def test_create_user(session: Session):
    username = "nick"
    birthday = datetime.now()

    result = create_user(session = session, username = username, birthday = birthday)
    print(result.username)

    assert result.username == username
    assert result.birthday == birthday
    assert result.id is not None
