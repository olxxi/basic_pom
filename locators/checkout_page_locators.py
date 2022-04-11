""" Locators for checkout page """

from selenium.webdriver.common.by import By


firstname_textbox = (By.ID, "first-name")
lastname_textbox = (By.ID, "last-name")
postalcode_textbox = (By.ID, "postal-code")
cancel_button = (By.CLASS_NAME, "cart_cancel_link")
continue_button = (By.CLASS_NAME, "btn_primary")
error_message = (By.CLASS_NAME, "error-button")
subheader = (By.CLASS_NAME, 'title')
