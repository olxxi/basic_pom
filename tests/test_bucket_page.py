""" Tests for bucket/cart page """

import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.bucket_page import BucketPage
from utils.creds_base import *


@pytest.mark.parametrize(
    "login, password",
    [
        (STANDARD_USER, STANDARD_PASSWORD),
        (PERFORMANCE_PROBLEM_USER, STANDARD_PASSWORD),
        (PROBLEM_USER, STANDARD_PASSWORD)
    ]
)
def test_remove_from_cart(driver, login, password):
    """
    Given a product in the cart
    When the user clicks the 'Remove' button
    Then the product is removed from the cart
    :param driver: webdriver object
    :param login: str - user's login
    :param password: str -user's pass
    """
    login_p = LoginPage(driver)
    login_p.perform_login_workflow(login, password)
    product_p = ProductPage(driver)
    product_p.add_all_to_cart()
    product_p.click_cart()
    cart_p = BucketPage(driver)
    cart_p.remove_all_items_from_cart()

    assert cart_p.get_sum_prices() == 0.0, "The sum of prices is not 0"
