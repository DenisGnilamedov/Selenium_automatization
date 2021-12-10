from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, 'This is not a login page!'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL), 'Login E-mail is not presented'
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD), 'Login password is not presented'
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL), 'Registration E-mail is not presented'
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD), 'Registration password is not presented'
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT), 'Registration password repeat ' \
                                                                                    'is not presented'
        assert True
