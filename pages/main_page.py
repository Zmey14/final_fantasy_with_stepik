from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        # изменить на подобии нижнего
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        # при добавлении разработчиками окна alert, они обрабатываются таким образом
        # alert = self.browser.switch_to.alert
        # alert.accept()

    # символ *, указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать. 
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not present!"