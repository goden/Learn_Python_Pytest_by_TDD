import pytest
import time

import pytest_html.extras
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


# === Selenium fixture ===
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# === pytest-html: 設定標題 ===
@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "自動化測試報告"

# === pytest-html: 加入 metadata ===
def pytest_configure(config):
    config.stash[metadata_key]["專案名稱"] = "自動化測試示範"
    config.stash[metadata_key]["測試環境"] = "UAT"
    config.stash[metadata_key]["瀏覽器"] = "Chrome"
    config.stash[metadata_key]["測試人員"] = "Gordon Cheng"


# === pytest-html: 每個測試附加資訊 (描述 + 耗時 + 截圖) ===
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    # 加入 docstring 當描述
    if report.when == "call":
        report.description = str(item.function.__doc__)

    # 加入測試耗時
    if hasattr(item, "start_time") and report.when == "call":
        duration = time.time() - item.start_time
        report.duration = round(duration, 2)

        if hasattr(report, "extra"):
            extra = report.extra
        else:
            extra = report.extra = []
        extra.append(pytest_html.extras.text(f"耗時: {report.duration} 秒"))

    # 測試失敗時，自動加截圖
    if report.failed and "browser" in item.fixturenames:
        browser = item.funcargs["browser"]
        screenshot_path = f"screenshot_{item.name}.png"
        browser.save_screenshot(screenshot_path)

        if hasattr(report, "extra"):
            extra = report.extra
        else:
            extra = report.extra = []

        extra.append(pytest_html.extras.png(screenshot_path))


# === 測試開始時間 (用來計算耗時) ===
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    item.start_time = time.time()
