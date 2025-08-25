import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

@pytest.fixture(name='driver')
def driver_fixture() -> Chrome:
    options = Options()
    options.add_argument('--start-maximized')

    driver = Chrome(options=options)
    yield driver

    driver.quit()