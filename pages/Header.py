from base.BaseDriver import BaseDriver
from locators.locators import HeaderLocators


class Header(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = HeaderLocators

    def get_signin_link(self):
        return self.find_element(*self.locator.SIGN_IN_LINK)
