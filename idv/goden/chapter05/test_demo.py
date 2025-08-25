import os
import time

from dotenv import load_dotenv
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv("C:/Users/goden/PycharmProjects/Learn_Python_Pytest_by_TDD/.env")

def test_demo_login(driver: Chrome):

    driver.get("https://hahow.in/")

    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[2]")
    login_button.click()
    time.sleep(10)

    login_form = driver.find_element(
        By.XPATH,
        "/html/body/div[6]/div/div/div/div/div/form"
    )
    input_tag_list = login_form.find_elements(By.CSS_SELECTOR, "input")

    # 預計會抓到兩個 input tag，第一個為帳號，第二個為密碼
    input_tag_list[0].send_keys(os.getenv("ACCOUNT"))
    input_tag_list[1].send_keys(os.getenv("PASSWORD"))
    input_tag_list[1].send_keys(Keys.ENTER)

    time.sleep(10)

    my_cursor_button = driver.find_element(
        By.CSS_SELECTOR,
        "li.my-courses-desktop.marg-rl-5"
    )

    assert "我的學習" in my_cursor_button.text

