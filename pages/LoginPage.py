from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage
from locators.login_page_locators import *


class LoginPage(BasePage):
    """
    Object for Login Page
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.init_site()

    def login_button_click(self):
        """
        Click on the login button.
        """
        self.click_element(login_button)
        WebDriverWait(self.driver, 5).until(EC.url_changes)

    def enter_password(self, password):
        """
        Enter a password into the password input field.
        """
        self.send_keys_to_element(input_password, password)

    def enter_username(self, username):
        """
        Enter a username into the username input field.
        """
        self.send_keys_to_element(input_username, username)

    def is_error_message_exists(self):
        """
        Returns true if an error message exists on the page, false otherwise.
        """
        error_message = self.driver.find_elements(*login_error_message)
        return len(error_message) > 0

    def get_error_message_text(self):
        """
        Returns the text of the error message on the page, if one exists.
        Returns None otherwise.
        """
        if self.is_error_message_exists():
            return self.driver.find_elements(*login_error_message)[0].text
        return None

    def perform_login_workflow(self, username, password):
        """
        Perform a complete login using username and password.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.login_button_click()
