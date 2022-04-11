import time
import pytest
from selenium import webdriver
from utils.constants import DEFAULT_WAIT_TIME


@pytest.fixture
def driver(request):
    """Creates test fixtures for pytest."""
    web_driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
    web_driver.delete_all_cookies()

    web_driver.implicitly_wait(DEFAULT_WAIT_TIME)
    # Maximize window to handle IC
    web_driver.maximize_window()
    # Return the driver object at the end of setup
    yield web_driver

    # For cleanup, quit the driver (after "yield" happens)
    web_driver.quit()



