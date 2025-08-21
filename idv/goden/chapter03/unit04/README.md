# pytest-html 介紹
## pytest-html 是什麼？
pytest-html 是 pytest 的外掛，可以在執行測試後自動產生 HTML 格式的測試報告，報告型式可包含：
- 測試結果（PASSED / FAILED / SKIPPED）
- 測試總覽與統計
- 失敗測試的詳細訊息與 traceback
- 可加入 截圖、log、環境資訊

## 安裝
```bash
    pip install pytest-html
```

## 基本用法
產生一份基本報告，執行後會在當前目錄下生成 report.html。
```bash
  pytest --html=report.html
```

## 加上 CSS / Log（更漂亮的報告）
你可以讓報告更完整，利用`--self-contained-html`屬性，把 CSS/JS 內嵌到報告中，方便單檔攜帶。
```bash
    pytest --html=report.html --self-contained-html
```

## 在測試中加入額外資訊
利用 pytest_html 的 hook，可以在測試過程中插入 log 或截圖。

例：在`conftest.py`加入hook

```python
import pytest

# 在報告中加上額外資訊
@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "我的測試報告"

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([pytest.html.html("專案: Demo System ")])
    postfix.extend([pytest.html.html("測試完成！")])

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    if report.failed:
        cells.insert(2, pytest.html.html("<td style='color:red'>❌ 失敗</td>"))

```

## 進階：在報告中加入截圖
常見於 UI 測試 (Selenium/Playwright)。

例：在測試失敗時附上截圖：

```python
import pytest

@pytest.fixture
def screenshot_on_failure(request):
    yield
    if request.node.rep_call.failed:
        # 假設這裡有一張測試截圖
        extra = getattr(request.node, "extra", [])
        extra.append(pytest.html.extras.png("screenshot.png"))
        request.node.extra = extra

```


