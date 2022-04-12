""" Cart/Bucket page object """

from pages.base_page import BasePage
from locators.bucket_locators import *


class BucketPage(BasePage):
    """
    Object for Cart Page
    """

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_checkout_button(self):
        """
        Click the checkout button.
        """
        self.click_element(checkout_button)

    def remove_all_items_from_cart(self):
        """
        Remove all items.
        """
        remove_buttons = self.driver.find_elements(*remove_button)
        while remove_buttons:
            remove = self.driver.find_element(*remove_button)
            remove.click()
            remove_buttons = self.driver.find_elements(*remove_button)

    def get_subheader(self):
        """
        Get the subheader text.
        """
        element = self.driver.find_element(*subheader)
        return element.text

    def get_sum_prices(self):
        """
        Return sum of all items in the cart.
        """
        price_elements = self.driver.find_elements(*item_price)
        total = 0.0
        for price in price_elements:
            total += float(price.text)
        return total
