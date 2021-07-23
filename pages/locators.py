from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    COASTBASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    COASTBOOK = (By.CSS_SELECTOR, ".product_main .price_color")