import pytest
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from pages.BucketPage import BucketPage
from pages.CheckoutPage import CheckoutPage
from utils.creds_base import *


@pytest.mark.parametrize(
    "login, password",
    [
        (STANDARD_USER, STANDARD_PASSWORD),
        (PERFORMANCE_PROBLEM_USER, STANDARD_PASSWORD),
        (PROBLEM_USER, STANDARD_PASSWORD)
    ]
)
def test_cancel_button(driver, login, password):
    """
    Given a product in the cart
    When the user clicks the 'CHECKOUT' button and go back
    Then the Cart appears
    :param driver: webdriver object
    :param login: str - user's login
    :param password: str -user's pass
    """
    login_page = LoginPage(driver)
    login_page.perform_login_workflow(login, password)
    product_page = ProductPage(driver)
    product_page.click_cart()
    cart_page = BucketPage(driver)
    cart_page.click_on_checkout_button()
    checkout_page = CheckoutPage(driver)
    checkout_page.click_cancel()

    assert cart_page.get_subheader() == "YOUR CART", "The cart page is not displayed."
