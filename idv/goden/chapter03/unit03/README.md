# pytest-mock 介紹
## pytest-mock 是什麼？
[pytest-mock](https://pypi.org/project/pytest-mock/) 是 pytest 的一個外掛，用來方便地使用 `unittest.mock` 的功能。提供`mocker fixture`，可以輕鬆地 `mock/patch` 函數、物件、方法。
它適合在測試中：
- 隔離依賴（例如外部 API、資料庫、檔案系統）
- 模擬回傳值 / 例外
- 驗證呼叫次數與參數

## 安裝
```bash
    pip install pytest-mock
```
## 基本用法
### mock函數回傳值
```python
# myapp/calculator.py
def add(a, b):
    return a + b

def use_add(x):
    return add(x, 10)
```
```python
# test_calculator.py
def test_use_add(mocker):
    
    mock_add = mocker.patch("myapp.calculator.add", return_value=99)
    result = use_add(5)
    
    assert result == 99
    
    mock_add.assert_called_once_with(5, 10)  # 驗證呼叫
```
### mock 物件方法
```python
class APIClient:
    def get_data(self):
        return {"status": "ok"}

def test_api_client(mocker):
    client = APIClient()
    mocker.patch.object(client, "get_data", return_value={"status": "mocked"})

    assert client.get_data() == {"status": "mocked"}
```

### 模擬例外
```python
import requests

def fetch(url):
    return requests.get(url)

def test_fetch_error(mocker):
    mocker.patch("requests.get", side_effect=Exception("Network error"))

    try:
        fetch("http://example.com")
    except Exception as e:
        assert str(e) == "Network error"
```

### 常見情境
- 測試不想真的呼叫外部 API 
- 測試不需要真的連線資料庫
- 測試不想真的存檔 / 刪檔
- 驗證函數是否被呼叫、呼叫幾次、用什麼參數

### 常用語法速查

| 語法                                    | 說明 |
|---------------------------------------|-|
| `mocker.patch("module.func")`         |mock 一個模組內的函數|
| `mocker.patch.object(obj, "method")`  |mock 一個物件的方法|
| `mocker.spy(obj, "method")`           |監控方法呼叫（不改變原邏輯）|
| `mock.return_value = ...`             |設定回傳值|
| `mock.side_effect = Exception("msg")` |模擬丟出例外| 
| `mock.assert_called_once()`           |驗證呼叫次數|
| `mock.assert_called_with(arg1, arg2)` |驗證呼叫參數|
