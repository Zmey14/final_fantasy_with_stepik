from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        
    # assert "/login" in self.open(), "login is absent in current url"
    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # self.is_element_present(*LoginPageLocators.LOGIN_PAGE), 'login page is not work'
        assert "/login" in self.browser.current_url, 'login page is not work'
        
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form is not find'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register form is not find'