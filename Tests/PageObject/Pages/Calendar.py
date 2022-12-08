
from Tests.PageObject.Locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import test_data
from time import sleep


class Calendar(object):
    # Login locators
    accept_terms_button = Locator.accept_button
    sign_in_button = Locator.sign_in_button
    email_field = Locator.email_field
    next_button = Locator.next_button
    password = Locator.password
    sign_in = Locator.sign_in

    # Homepage locators
    finance = Locator.finance_button
    market_data = Locator.market_data_button
    calendar = Locator.calendar_button
    next_calendar_page = Locator.next
    date_events = Locator.events

    def __init__(self, driver):
        self.driver = driver

    # Login to account
    def click_accept_button(self):
        self.driver.find_element(By.XPATH, self.accept_terms_button).click()

    def click_sign_in_button(self):
        self.driver.find_element(By.XPATH, self.sign_in_button).click()

    def enter_email(self):
        self.driver.find_element(By.XPATH, self.email_field).clear()
        self.driver.find_element(By.XPATH, self.email_field).send_keys(test_data.valid_username)

    def click_next_button(self):
        self.driver.find_element(By.XPATH, self.next_button).click()

    def enter_password(self):
        self.driver.find_element(By.NAME, self.password).clear()
        self.driver.find_element(By.NAME, self.password).send_keys(test_data.valid_password)

    def click_sign_in(self):
        self.driver.find_element(By.XPATH, self.sign_in).click()

    # Go to Finance page
    def click_finance(self):
        self.driver.find_element(By.XPATH, self.finance).click()

    # Hover mouse over market_data to display options
    def show_market_data(self):
        m_data = self.driver.find_element(By.XPATH, self.market_data)
        a_chains = ActionChains(self.driver)
        a_chains.move_to_element(m_data).perform()
        sleep(2)

    # Select calendar option
    def select_calendar(self):
        self.driver.find_element(By.XPATH, self.calendar).click()
        sleep(2)

    # Click next button on calendar
    def click_next_calendar_page(self):
        self.driver.find_element(By.XPATH, self.next_calendar_page).click()
        sleep(2)

    # Get 12th of Dec events
    def get_events(self):
        event = self.driver.find_element(By.XPATH, self.date_events)
        return event





