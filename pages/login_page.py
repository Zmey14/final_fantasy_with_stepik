from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from faker import Faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        
    # assert "/login" in self.open(), "login is absent in current url"
    def should_be_login_url(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        assert "/login" in self.browser.current_url, 'login page is not work'
        
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form is not find'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register form is not find'

    def register_new_user(self):
        f = Faker()
        email = f.email()
        password = f.password()
        email_reg = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_reg.send_keys(email)
        password1_reg = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password1_reg.send_keys(password)
        password2_reg = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2_reg.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button.click()