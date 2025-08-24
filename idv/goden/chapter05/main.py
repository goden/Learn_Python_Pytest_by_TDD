import time
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

# entry to the program context
if __name__ == '__main__':
    chrome_driver = create_chrome_driver()
    #request_ptt_boards(driver=chrome_driver)
    #get_ptt_boards_by_css(chrome_driver)
    get_ptt_boards_by_xpath(chrome_driver)
    chrome_driver.quit()





