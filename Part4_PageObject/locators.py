from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn:first-child')


class BasketPageLocators():
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner>p')
    ITEM_IN_BASKET = (By.CLASS_NAME, 'basket-title')


class LoginPageLocators():
    LOGIN_EMAIL = (By.ID, 'id_login-username')
    LOGIN_PASSWORD = (By.ID, 'id_login-password')
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD_REPEAT = (By.ID, 'id_registration-password2')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class ProductPageLocators():
    ADD_TO_CART = (By.CLASS_NAME, 'btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, '.col-sm-6 h1')
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    ITEM_COST = (By.CSS_SELECTOR, '.col-sm-6 p.price_color')
    ADDED_ITEM_COST = (By.CSS_SELECTOR, '#messages div:nth-child(3) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-of-type(2)')

