from selenium.webdriver.support.select import Select
from base.BaseDriver import BaseDriver
from locators.locators import RegisterPageLocators


class RegisterPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = RegisterPageLocators

    def get_user_id_field(self):
        return self.find_element(*self.locator.USER_ID_FIELD)

    def get_new_password_field(self):
        return self.find_element(*self.locator.NEW_PASSWORD_FIELD)

    def get_repeated_password_field(self):
        return self.find_element(*self.locator.REPEATED_PASSWORD_FIELD)

    def get_first_name_field(self):
        return self.find_element(*self.locator.FIRST_NAME_FIELD)

    def get_last_name_field(self):
        return self.find_element(*self.locator.LAST_NAME_FIELD)

    def get_email_field(self):
        return self.find_element(*self.locator.EMAIL_FIELD)

    def get_phone_field(self):
        return self.find_element(*self.locator.PHONE_FIELD)

    def get_address1_field(self):
        return self.find_element(*self.locator.ADDRESS1_FIELD)

    def get_address2_field(self):
        return self.find_element(*self.locator.ADDRESS2_FIELD)

    def get_city_field(self):
        return self.find_element(*self.locator.CITY_FIELD)

    def get_state_field(self):
        return self.find_element(*self.locator.STATE_FIELD)

    def get_zip_field(self):
        return self.find_element(*self.locator.ZIP_FIELD)

    def get_country_field(self):
        return self.find_element(*self.locator.COUNTRY_FIELD)

    def get_language_preference_field(self):
        return self.find_element(*self.locator.LANGUAGE_PREFERENCE_SELECT_LIST)

    def get_favourite_category_field(self):
        return self.find_element(*self.locator.FAVOURITE_CATEGORY_SELECT_LIST)

    def get_my_list_checkbox(self):
        return self.find_element(*self.locator.ENABLE_MY_LIST_CHECKBOX)

    def get_my_banner_checkbox(self):
        return self.find_element(*self.locator.ENABLE_MY_BANNER_CHECKBOX)

    def get_new_account_button(self):
        return self.find_element(*self.locator.NEW_ACCOUNT_BUTTON)

    def register(self, user_id, new_pass, re_pass, f_name, l_name, email, phone, address1, address2, city, state, zip_c,
                 country, lang, fav_category, my_list, my_banner):
        self.get_user_id_field().send_keys(user_id)
        self.get_new_password_field().send_keys(new_pass)
        self.get_repeated_password_field().send_keys(re_pass)
        self.get_first_name_field().send_keys(f_name)
        self.get_last_name_field().send_keys(l_name)
        self.get_email_field().send_keys(email)
        self.get_phone_field().send_keys(phone)
        self.get_address1_field().send_keys(address1)
        self.get_address2_field().send_keys(address2)
        self.get_city_field().send_keys(city)
        self.get_state_field().send_keys(state)
        self.get_zip_field().send_keys(zip_c)
        self.get_country_field().send_keys(country)
        select_language = Select(self.get_language_preference_field())
        select_language.select_by_value(lang)
        select_fav_category = Select(self.get_favourite_category_field())
        select_fav_category.select_by_value(fav_category)
        if my_list == "true":
            self.get_my_list_checkbox().click()
        if my_banner == "true":
            self.get_my_banner_checkbox().click()
        self.get_new_account_button().click()
