import time

from prompt_toolkit.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def create_chrome_driver() -> Chrome:
    return Chrome()

def request_ptt_boards(driver: Chrome):
    url = "https://www.ptt.cc/bbs/index.html"
    driver.get(url)
    time.sleep(10)

def get_ptt_boards_by_css(driver: Chrome):
    url = "https://www.ptt.cc/bbs/index.html"
    driver.get(url)

    css_string = "div.board-name"

    # 尋找第一個 board-name 元素
    board_element = driver.find_element(By.CSS_SELECTOR, css_string)
    print(board_element.text)

    # 尋找全部的 board-name
    board_element_list = driver.find_elements(By.CSS_SELECTOR, css_string)
    print([tmp_element.text for tmp_element in board_element_list])

def get_ptt_boards_by_xpath(driver: Chrome):
    url = "https://www.ptt.cc/bbs/index.html"
    driver.get(url)

    first_board_xpath_string = "/html/body/div[2]/div[2]/div[1]/a/div[1]"
    board_element = driver.find_element(By.XPATH, first_board_xpath_string)

    print(board_element.text)

    all_board_xpath_string = "/html/body/div[2]/div[2]/div/a/div[1]"
    board_element_list = driver.find_elements(By.XPATH, all_board_xpath_string)

    print([tmp.text for tmp in board_element_list])

def get_basic_page_message(driver: Chrome):
    url = "https://www.ptt.cc/bbs/index.html"
    driver.get(url)

    print(driver.title)
    print(driver.current_url)

def demo_click_element(driver: Chrome):
    url = "https://www.ptt.cc/bbs/index.html"

    driver.get(url)
    gossiping_board_tag = driver.find_element(By.CSS_SELECTOR, "a.board")
    gossiping_board_tag.click()
    time.sleep(5)

    driver.get(url)
    gossiping_board_tag = driver.find_element(By.CSS_SELECTOR, "a.board")
    driver.execute_script("arguments[0].click();", gossiping_board_tag)
    time.sleep(5)

def demo_scroll_page(driver: Chrome):
    url = "https://www.ptt.cc/bbs/index.html"
    driver.get(url)
    time.sleep(5)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(5)

def demo_keyboard_action(driver: Chrome):
    url = "https://www.google.com.tw/?hl=zh_TW"
    driver.get(url)

    search_bar = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div[4]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea"
    )

    search_text = "Hahow"
    for i in search_text:
        search_bar.send_keys(i)
        time.sleep(1)

    from selenium.webdriver.common.keys import Keys
    search_bar.send_keys(Keys.ENTER)
    time.sleep(20)



# entry to the program context
if __name__ == '__main__':
    chrome_driver = create_chrome_driver()
    # request_ptt_boards(driver=chrome_driver)
    # get_ptt_boards_by_css(chrome_driver)
    # get_ptt_boards_by_xpath(chrome_driver)
    # get_basic_page_message(chrome_driver)
    # demo_click_element(chrome_driver)
    # demo_scroll_page(chrome_driver)
    demo_keyboard_action(chrome_driver)
    chrome_driver.quit()





