from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_add_to_cart_and_verify(self):
        self.add_to_cart()
        self.added_item_matches_required_item()
        self.cart_cost_matches_item_cost()

    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()

    def added_item_matches_required_item(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        added_item = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text
        assert item_name == added_item, 'Names don`t match!'

    def cart_cost_matches_item_cost(self):
        item_cost = self.browser.find_element(*ProductPageLocators.ITEM_COST).text
        added_item_cost = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_COST).text
        assert item_cost == added_item_cost, 'Cost doesn`t match!'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but has not"
