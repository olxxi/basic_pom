## Selenium Page Object Model framework implementation

Basic implementation of POM automation testing framework for https://www.saucedemo.com/.

### Structure:
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
