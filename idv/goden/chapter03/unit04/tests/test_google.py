def test_google_search(browser):
    """驗證 Google 首頁標題"""
    browser.get("https://www.google.com")
    assert "Google" in browser.title


def test_google_fail(browser):
    """這個測試故意失敗，產生截圖"""
    browser.get("https://www.google.com")
    assert "Bing" in browser.title
