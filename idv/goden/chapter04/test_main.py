from idv.goden.chapter04.main import get_ptt_boards, insert_ptt_board
from idv.goden.chapter04.models import Board


def test_get_ptt_board():
    expected = "Stock"

    result = get_ptt_boards()
    print(result)

    assert expected in result


def test_insert_ptt_board(sqlite_session):
    expected = "test"

    insert_ptt_board(name=expected, session=sqlite_session)

    assert sqlite_session.query(Board).first().name == expected
