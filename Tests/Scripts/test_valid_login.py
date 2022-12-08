import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.ValidLogin import LoginPage
import test_data
from time import sleep


class TestValidLogin(EnvironmentSetup):

    def test_valid_login(self):
        login = LoginPage(self.driver)

        login.click_accept_button()

        login.click_sign_in_button()
        login.enter_email()
        login.click_next_button()
        login.enter_password()
        login.click_sign_in()
        assert login.check_logout_button().text == 'Sign out'







