from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def basket_empty(self):
        # Как только к нам в корзину попадёт товар, тест упадёт
        assert self.is_not_element_present(*BasePageLocators.BASKET_EMPTY), "The basket is not empty!"

    def basket_not_empty_text(self):
        # Проверка на то, что у нас есть текс подтверждающий что наша корзина пустая
        assert self.browser.find_element(*BasePageLocators.BASKET_EMPTY_TEXT).text, "Text not find!"
        
 