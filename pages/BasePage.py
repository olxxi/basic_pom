from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.creds_base import URL


class BasePage:
    """ Page class. """
    def __init__(self, driver):
        self.driver = driver
        self.url = URL

    def init_site(self):
        """ Initialize the URL. """
        self.driver.get(self.url)

    def click_element(self, selector, wait_time=5):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(selector)
        )
        element.click()

    def send_keys_to_element(self, selector, text, wait_time=5):
        """ Enter a username into the username textbox. """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(selector)
        )
        element.send_keys(text)
