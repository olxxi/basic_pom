""" Tests for the product page. """

import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.creds_base import *


@pytest.mark.parametrize(
    "login, password",
    [
        (STANDARD_USER, STANDARD_PASSWORD),
        (PERFORMANCE_PROBLEM_USER, STANDARD_PASSWORD),
        (PROBLEM_USER, STANDARD_PASSWORD)
    ]
)
def test_get_product_list(driver, login, password):
    """
    Given a user with a valid login and password,
    When the user is on the login page,
    Then the user can login successfully and see the product list

    :param driver: webdriver object
    :param login: str - user's login
    :param password: str -user's pass
    """
    login_p = LoginPage(driver)
    login_p.perform_login_workflow(login, password)
    product_p = ProductPage(driver)
    product_names = product_p.get_list_of_product_names()

    assert len(product_names) > 0, "Cannot find the product list"
