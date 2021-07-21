from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # EMAIL_REG = (By.CSS_SELECTOR, "[for='id_registration-email']")
    # PASSWORD1_REG = (By.CSS_SELECTOR, "[for='id_registration-password1']")
    # PASSWORD2_REG = (By.CSS_SELECTOR, "[for='id_registration-password2']")
    # EMAIL_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    # PASSWORD1_LOGIN = (By.CSS_SELECTOR, "#id_login-password")
    # LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")