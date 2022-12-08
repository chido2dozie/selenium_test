import pytest
from selenium.common.exceptions import *
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.InvalidLogin import InvalidLogin
from time import sleep


class TestInvalidLogin(EnvironmentSetup):

    def test_invalid_login(self):
        login = InvalidLogin(self.driver)

        try:
            login.click_accept_button()

            login.click_sign_in_button()
            login.enter_email()
            login.click_next_button()
            login.enter_password()
            login.click_sign_in()
            sleep(2)
        except NoSuchElementException:
            print("Email address entered is not valid!")

