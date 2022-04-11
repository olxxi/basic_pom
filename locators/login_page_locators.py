""" Login page locators """

from selenium.webdriver.common.by import By


input_username = (By.ID, "user-name")
input_password = (By.ID, "password")
login_button = (By.CLASS_NAME, "btn_action")
login_error_message = (By.XPATH, '//*[@id="login_button_container"]/div/form')
