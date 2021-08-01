from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_in_basket(self):
        submit = self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        submit.click()

    def shopping_cart_comparison_price(self):
        coast_basket = self.browser.find_element(*ProductPageLocators.COASTBASKET).text
        coast_book = self.browser.find_element(*ProductPageLocators.COASTBOOK).text
        assert coast_basket == coast_book, "цены не соответствуют друг другу"

    def shopping_cart_comparison_title(self):
        name_title = self.browser.find_element(*ProductPageLocators.NAMETITLEBOOK).text
        name_book = self.browser.find_element(*ProductPageLocators.NAMEBOOK).text
        assert name_book == name_title, "Названия книги отличаются"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_desappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Element is desappaered"

   
