from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email.form-control")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1.form-control")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2.form-control")
    BUTTON_REGISTER = (By.CSS_SELECTOR, ".register_form .btn-lg")


class ProductPageLocators():
    NAMEBOOK = (By.CSS_SELECTOR, ".product_main h1")
    NAMETITLEBOOK = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    COASTBASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    COASTBOOK = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")
    TESTS = (By.CSS_SELECTOR, ".btn-add-to-basket")
    

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    OPEN_BASKET =(By.CSS_SELECTOR, "span a.btn-default") 
    BASKET_EMPTY = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    
