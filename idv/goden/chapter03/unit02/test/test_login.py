import pytest

from idv.goden.chapter03.unit02.action.login import do_login


@pytest.mark.parametrize(
    argnames="username, password, expected",
    argvalues=[
        ["goden", "1234", "ogin successfully!"],
        ["nick", "1234", "Username is wrong!"],
        ["goden", "1235", "Password is wrong!"]
    ],
    ids=[1, 2, 3]
)
def test_login(username, password, expected):
    if isinstance(expected, str):
        result = do_login(username = username, password = password)

        print(result)
        assert result == expected

    else:
        with pytest.raises(expected) as exec:
            do_login(username = username, password = password)

        print(exec.value.__class__)
        assert exec.value.__class__ == expected