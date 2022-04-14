## Selenium Page Object Model framework

Basic implementation of POM automation testing framework for https://www.saucedemo.com/.

Page-object-model (POM) is a pattern that you can apply it to develop efficient automation framework. With page-model, it is possible to minimise maintenance cost. Basically page-object means that your every page is inherited from a base class which includes basic functionalities for every pages. If you have some new functionality that every pages have, you can simple add it to the base class.

`BasePage` class (`pages.base_page.py`) include basic functionality and driver initialization:

```python
class BasePage:
    """ Page class. """
    def __init__(self, driver):
        self.driver = driver
        self.url = URL

    def init_site(self):
        """ Initialize the URL. """
        self.driver.get(self.url)

    def click_element(self, selector, wait_time=5):
        """ Click on an element. """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(selector)
        )
        element.click()
        
     ...
```

For example, `LoginPage` (`pages.login_page.py`) class is derived from th `BasePage` class. It contains methods related to this page, which will be used to create test steps.

```python
class LoginPage(BasePage):
    """
    Object for Login Page
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.init_site()

    def login_button_click(self):
        """
        Click on the login button.
        """
        self.click_element(login_button)
        WebDriverWait(self.driver, 5).until(EC.url_changes)
       
    ...
```

In the process of writing tests, you should base you workflow in actions described in the page classes:

```python
def test_successful_login(driver, login, password):

    login_page = LoginPage(driver)
    login_page.enter_username(login)
    login_page.enter_password(password)
    login_page.login_button_click()

    assert not login_page.is_error_message_exists()
```
---
### Project Structure:
* Locators: `locators/*`
* Pages: `pages/*`
* Tests: `tests/*`
* Constants/Credentials: `utils/*`
* WebDriver storage: `drivers/*`

### Usage:
1. Install the dependencies:

    `pip install -r requirements.txt`

2. Run the tests:

    `pytest -v`

3. Run the tests in parallel:

    `pytest -v -n 4`
4. Run static check for the code. The configuration is in `.pylintrc` file.

    `pylint ./folder_name/*`

### Description:

**Locators**

Each file under `locators` directory represents a set of selectors for a particular page. The basic structure could be described as `selector = (By.#, 'selector')`. All selectors should be imported to the page object class for the further usage.

**Pages**

The pages under `pages` directory are the classes that represent the web pages. Each page class should be imported to the test file and used for the required actions. Because of that, Page Object Model allows to use the same page class for different tests and setup new tests simply and quickly without a lot of programming experience.

**Tests**

    * `tests/test_login.py` - tests the login functionality
    * `tests/test_logout.py` - tests the logout functionality
    * `tests/test_add_to_cart.py` - tests the add to cart functionality
    * `tests/test_checkout.py` - tests the checkout functionality

Each test file stands for testing particular page on a target site. Contents could be represented either as a test class or as test functions like in the current example. 

**Utilities**

Utilities storage is a place to store all kind of project constants, helpers, utility functions (e.g. cleanup, logging,etc.).

**Drivers storage**

Depending on the project and requirements, one of the option is to use a local storage for webdrivers. If you are going to extent the testing requirements in terms of crossbrowser testing, then you might want to switch over to distributed solutions like Selenium Grid, Selenoid, etc. Or use a webdriver manager.
