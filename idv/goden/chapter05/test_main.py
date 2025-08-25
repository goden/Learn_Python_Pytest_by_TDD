import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def test_ptt_gossiping_paragraph(driver: Chrome):
    url = "https://www.ptt.cc/bbs/index.html"
    driver.get(url)
    time.sleep(5)

    gossiping_tag = driver.find_element(By.CSS_SELECTOR, "a.board")
    gossiping_tag.click()

    # 驗證是否跳轉到驗證頁面
    assert driver.current_url.startswith("https://www.ptt.cc/ask/over18")

    agree_button = driver.find_element(By.CSS_SELECTOR, "button.btn-big")
    agree_button.click()
    time.sleep(5)

    assert driver.current_url == "https://www.ptt.cc/bbs/Gossiping/index.html"

    paragraph_element_list = driver.find_elements(By.CSS_SELECTOR, "div.title")
    paragraph_title_list = [
        tmp.text for tmp in paragraph_element_list
    ]

    print(paragraph_title_list)

    assert paragraph_title_list is not None