from pytest_mock import MockFixture

from idv.goden.chapter03.unit03.demos import demo


def test_get_ptt_boards(mocker: MockFixture):
    class TmpResponse:
        text = "<div class='board-name'>Test</div>"

    mocker.patch(
        target = "requests.get",
        return_value = TmpResponse
    )

    result = demo.get_ptt_boards()
    print(result)

    assert "Test" in result