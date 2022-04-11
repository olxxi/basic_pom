""" Locators for Product List Page """

from selenium.webdriver.common.by import By


add_to_cart_buttons_selector = (By.CLASS_NAME, "btn_primary")

hamburger_menu_selector = (
    By.CSS_SELECTOR, "#menu_button_container > div > div:nth-child(3) > div > button"
)

cart_item_count_selector = (By.CLASS_NAME, "shopping_cart_badge")

cart_selector = (By.CLASS_NAME, "shopping_cart_link")

inventory_item_name_selector = (By.CLASS_NAME, "inventory_item_name")

inventory_item_price_selector = (By.CLASS_NAME, "inventory_item_price")

inventory_item_selector = (By.CLASS_NAME, "inventory_item")

inventory_list_selector = (By.CLASS_NAME, "inventory_list")

sort_a_to_z_selector = (
    By.CSS_SELECTOR, "#inventory_filter_container > select > option:nth-child(1)"
)

sort_z_to_a_selector = (
    By.CSS_SELECTOR, '#inventory_filter_container > select > option:nth-child(2)'
)

sort_low_to_high_selector = (
    By.CSS_SELECTOR, "#inventory_filter_container > select > option:nth-child(3)"
)

sort_high_to_low_selector = (
    By.CSS_SELECTOR, "#inventory_filter_container > select > option:nth-child(4)"
)

sort_menu_selector = (
    By.CSS_SELECTOR, "#inventory_filter_container > select"
)

ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")

URL_XPATH = ".//div[2]/a"

subheader_selector = (By.CLASS_NAME, 'product_label')
