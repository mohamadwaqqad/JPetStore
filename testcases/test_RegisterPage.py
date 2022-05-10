import unittest
import pytest
from ddt import ddt, data, unpack

from pages.Header import Header
from pages.RegisterPage import RegisterPage
from pages.SignInPage import SignInPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
@ddt
class TestRegisterPage(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils()
        self.hd = Header(self.driver)
        self.sin = SignInPage(self.driver)
        self.reg = RegisterPage(self.driver)

    @data(*Utils.read_data_from_excal("RegisterData"))
    @unpack
    def test_invalid_register(self, user_id, new_pass, re_pass, f_name, l_name, email, phone, address1, address2, city,
                              state, zip_c, country, lang, fav_category, my_list, my_banner):
        """Register with invalid data"""
        self.hd.get_signin_link().click()
        self.sin.get_register_now_link().click()
        self.reg.register(user_id, new_pass, re_pass, f_name, l_name, email, phone, address1, address2, city, state,
                          zip_c, country, lang, fav_category, my_list, my_banner)
