from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_basket_be_empty(self):
        self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY)
        self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET)

