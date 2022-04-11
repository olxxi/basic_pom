from pages.BasePage import BasePage
from locators.checkout_page_locators import *


class CheckoutPage(BasePage):
    """
    Object for Checkout page
    """

    def __init__(self, driver):
        super().__init__(driver)

    def input_first_name(self, name):
        """
        Input the first name.
        """
        self.send_keys_to_element(firstname_textbox, name)

    def input_last_name(self, name):
        """
        Input the last name.
        """
        self.send_keys_to_element(lastname_textbox, name)

    def input_postal_code(self, postal_code):
        """
        Input the postal code.
        """
        self.send_keys_to_element(postalcode_textbox, postal_code)

    def get_first_name(self):
        """
        Get the text entered into the first name input textbox.
        """
        element = self.driver.find_element(*firstname_textbox)
        return element.get_attribute("value")

    def get_last_name(self):
        """
        Get the text entered into the last name input textbox.
        """
        element = self.driver.find_element(*lastname_textbox)
        return element.get_attribute("value")

    def click_cancel(self):
        """
        Click the cancel button. (Returns to cart page.)
        """
        self.click_element(cancel_button)

    def click_continue(self):
        """
        Click the continue button. (Goes to Checkout Overview page.)
        """
        self.click_element(continue_button)

    def get_subheader(self):
        """
        Get the subheader text.
        """
        element = self.driver.find_element(*subheader)
        return element.text
