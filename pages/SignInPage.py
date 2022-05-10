from locators.locators import SignInPageLocators
from base.BaseDriver import BaseDriver


class SignInPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = SignInPageLocators

    def get_user_name_field(self):
        return self.find_element(*self.locator.USER_NAME_FIELD)

    def get_password_field(self):
        return self.find_element(*self.locator.PASSWORD_FIELD)

    def get_login_button(self):
        return self.find_element(*self.locator.LOGIN_BUTTON)

    def get_register_now_link(self):
        return self.find_element(*self.locator.REGISTER_LINK)

    def get_error_message(self):
        return self.find_element(*self.locator.ERROR_MESSAGE)

    def signin(self, uname, password):
        self.get_user_name_field().send_keys(uname)
        self.get_password_field().clear()
        self.get_password_field().send_keys(password)
        self.get_login_button().click()

    def error_message_is_dis(self):
        return self.get_error_message().is_displayed()
