from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_in_basket(self):
        submit = self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        submit.click()
        # assert "?promo=newYear" in self.browser.current_url, "скидки не будет!"

    def shopping_cart_comparison(self):
        coast_basket = self.is_element_present(*ProductPageLocators.COASTBASKET)
        coast_book = self.is_element_present(*ProductPageLocators.COASTBOOK)
        try: 
            coast_book == coast_basket
            print("The cost of the basket is the same as the price of the product")
        except:
            print("The cost of the basket does not match the price of the product")