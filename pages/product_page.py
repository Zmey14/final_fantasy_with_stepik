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
        # try: 
        #     if name_book == name_title:
        #         print("The cost of the basket is the same as the price of the product")
                
        #     else:
        #         print("The cost of the basket does not match the price of the product")
        # except:
        #     'Такой элемент отсутствует'
        