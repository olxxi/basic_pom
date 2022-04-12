""" Tests for the Login page. """

import pytest
from pages.login_page import LoginPage
from utils.creds_base import *


@pytest.mark.parametrize(
    "login, password",
    [
        (STANDARD_USER, STANDARD_PASSWORD),
        (PERFORMANCE_PROBLEM_USER, STANDARD_PASSWORD),
        (PROBLEM_USER, STANDARD_PASSWORD)
    ]
)
def test_successful_login(driver, login, password):
    """
    Given a login/password information
    When a user inputs a valid credentials on the Login Page
    Then the user successfully logged in
    :param driver: webdriver object
    :param login: str - user's login
    :param password: str -user's pass
    """
    login_page = LoginPage(driver)
    login_page.enter_username(login)
    login_page.enter_password(password)
    login_page.login_button_click()

    assert not login_page.is_error_message_exists()
