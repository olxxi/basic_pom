from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
from locators.product_list_locators import *


class ProductPage(BasePage):
    """
    Object for Product List page
    """

    def __init__(self, driver):
        super().__init__(driver)

    def click_cart(self):
        """
        Click the cart button.
        """
        self.click_element(cart_selector)

    def click_hamburger_menu(self):
        """
        Open the hamburger menu.
        """
        self.click_element(hamburger_menu_selector)

    def click_product_sort_menu(self):
        """
        Click the product sort menu.
        """
        self.click_element(sort_menu_selector)

    def get_add_to_cart_buttons(self):
        """
        Get the element of all add to cart buttons.
        """
        buttons = self.driver.find_elements(*add_to_cart_buttons_selector)
        return buttons

    def get_all_product_elements(self):
        """
        Get the element of all products
        """
        products = self.driver.find_elements(*inventory_item_selector)
        return products

    def get_list_of_product_names(self):
        """
        Get the name of all products on the Product list page.
        """
        products = self.driver.find_elements(*inventory_item_name_selector)
        return [item.text for item in products]

    def get_subheader(self):
        """
        Get the subheader text. Used to assert that the driver is on the cart page.
        """
        element = self.driver.find_element(*subheader_selector)
        return element.text

    def get_number_cart_items(self):
        """
        Get the number of items in the cart.
        """
        has_items_in_cart = len(self.driver.find_elements(*cart_item_count_selector)) > 0
        if has_items_in_cart:
            num_items_in_cart = self.driver.find_element(*cart_item_count_selector).text
            return int(num_items_in_cart)
        else:
            return 0

    def add_all_to_cart(self):
        """
        Add all products to the cart.
        """
        product_elements = self.get_all_product_elements()
        for product in product_elements:
            add_cart_button = product.find_element(*ADD_TO_CART_BUTTON)
            add_cart_button.click()
