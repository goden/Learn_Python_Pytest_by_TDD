import pytest

from idv.goden.chapter03.unit03.app import service


def test_sync_user_success(mocker):
    # 1. Mock API 回傳
    mock_api = mocker.patch("myapp.api.fetch_user", return_value={"id": 1, "name": "Alice"})

    # 2. Mock DB save 方法
    mock_db = mocker.patch("myapp.db.Database.save_user", return_value=True)

    result = service.sync_user(1)

    # 驗證結果
    assert result is True
    mock_api.assert_called_once_with(1)
    mock_db.assert_called_once_with({"id": 1, "name": "Alice"})


def test_sync_user_api_error(mocker):
    # 模擬 API 發生錯誤
    mocker.patch("myapp.api.fetch_user", side_effect=Exception("API down"))

    with pytest.raises(Exception, match="API down"):
        service.sync_user(2)


def test_sync_user_db_fail(mocker):
    # API 正常
    mocker.patch("myapp.api.fetch_user", return_value={"id": 2, "name": "Bob"})
    # DB 存失敗
    mocker.patch("myapp.db.Database.save_user", return_value=False)

    result = service.sync_user(2)
    assert result is False
