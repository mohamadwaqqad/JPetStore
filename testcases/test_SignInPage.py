import unittest
import pytest
from ddt import ddt, data, unpack
from pages.Header import Header
from pages.SignInPage import SignInPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
@ddt
class TestSignInPage(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils()
        self.hd = Header(self.driver)
        self.sin = SignInPage(self.driver)

    def test_valid_signin(self) -> None:
        """Login with valid username and password"""
        self.hd.get_signin_link().click()
        self.sin.signin("waqqad33", "1234567")

    @data(*Utils.read_data_from_excal("SignInData"))
    @unpack
    def test_invalid_signin(self, username, password, error_message):
        """Login with invalid username or invalid password or both"""
        self.hd.get_signin_link().click()
        self.sin.signin(username, password)
        expect_result = self.sin.error_message_is_dis()
        self.assertTrue(expect_result, error_message)
