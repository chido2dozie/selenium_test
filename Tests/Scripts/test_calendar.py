import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Tests.TestBase.EnvironmentSetup import EnvironmentSetup
from Tests.PageObject.Pages.Calendar import Calendar
import test_data
from time import sleep


class TestCalendar(EnvironmentSetup):

    # Test that user with valid credentials can log in successfully
    def test_calendar(self):
        # Create an object to call Calendar page methods
        calendar_event = Calendar(self.driver)

        calendar_event.click_accept_button()

        calendar_event.click_sign_in_button()
        calendar_event.enter_email()
        calendar_event.click_next_button()
        calendar_event.enter_password()
        calendar_event.click_sign_in()
        calendar_event.click_finance()
        calendar_event.show_market_data()
        calendar_event.select_calendar()
        calendar_event.click_next_calendar_page()
        assert calendar_event.get_events().text == "Earnings"


