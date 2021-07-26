from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    NAMEBOOK = (By.CSS_SELECTOR, ".product_main h1")
    NAMETITLEBOOK = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    COASTBASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    COASTBOOK = (By.CSS_SELECTOR, ".product_main .price_color")
