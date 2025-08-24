# Selenium
## Selenium是什麼
Selenium 是一套瀏覽器自動化測試框架，用來模擬使用者操作瀏覽器，最常見用途是：
- 自動化網站功能測試（Functional/E2E Test）
- 爬蟲（Web Scraping，雖然官方定位是測試框架）
- 回歸測試（Regression Test）

## 核心組件
- Selenium WebDriver
    - 透過程式控制瀏覽器
    - 支援 Chrome、Firefox、Edge、Safari
    - 需要對應的驅動程式 (Driver)
- Selenium Grid
  - 分散式測試（多台機器同時跑）
  - CI/CD Pipeline 常用

## 安裝
```bash
    pip install selenium
```
還需要下載對應 瀏覽器驅動程式：

| Browser | Website                                                                                                    | Download                                                                                                     |
|---------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Chrome  | [Chrome for Testing Availability](https://developer.chrome.com/docs/chromedriver?hl=zh-tw)                 | [Downloads](https://googlechromelabs.github.io/chrome-for-testing/)                                          |
| Edge    | [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver?form=MA13LH) | [Stable Channel](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver?form=MA13LH#downloads) |
| Firefox | [WebDriver for Firefox](https://github.com/mozilla/geckodriver) | [Downloads](https://github.com/mozilla/geckodriver/releases)                                                                                                    |
| Safari  | [WebDriver Support in Safari 10](https://webkit.org/blog/6900/webdriver-support-in-safari-10/) | [Webkit Download](https://webkit.org/downloads/)                                                             |
把 driver 路徑加到 環境變數 PATH，程式才能找到。

## 基本範例
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 啟動 Chrome
driver = webdriver.Chrome()

# 開啟 Google
driver.get("https://www.google.com")

# 找到搜尋框，輸入關鍵字
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.submit()

# 等待 3 秒觀察結果
time.sleep(3)

# 驗證標題
assert "Selenium Python" in driver.title

# 關閉
driver.quit()

```
## 元素定位方式
`find_element(By, value)` → 常見定位法：
- `By.ID` → `driver.find_element(By.ID, "username")`
- `By.NAME` → `driver.find_element(By.NAME, "q")`
- `By.CLASS_NAME` → `driver.find_element(By.CLASS_NAME, "btn")`
- `By.TAG_NAME` → `driver.find_element(By.TAG_NAME, "input")`
- `By.CSS_SELECTOR` → `driver.find_element(By.CSS_SELECTOR, "div.container > button")`
- `By.XPATH` → `driver.find_element(By.XPATH, "//input[@type='text']")`

## 操作
```python
element.click()           # 點擊
element.send_keys("text") # 輸入文字
element.clear()           # 清空輸入框
driver.back()             # 返回上一頁
driver.refresh()          # 重新整理
```

## 等待機制
避免元素未載入導致找不到的局面：
### 強制等待
```python
import time
time.sleep(3)
```

### 顯式等待 (Explicit Wait)
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "username")))

```

## 與Pytest的整合
可以撰寫UI測試，搭配`pytest-html`產生報告:
```python
def test_google_search(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("pytest selenium")
    search_box.submit()
    assert "pytest selenium" in browser.title

```

## 適用情境
✅ 網站自動化測試：登入、購物車、表單送出

✅ CI/CD 測試：GitLab CI / Jenkins 上跑回歸測試

✅ 簡單爬蟲：處理需要 JavaScript 的頁面


❌ 大量資料爬蟲：效能比不上 requests + BeautifulSoup

❌ 桌面應用測試：那要用 PyAutoGUI 或 WinAppDriver
