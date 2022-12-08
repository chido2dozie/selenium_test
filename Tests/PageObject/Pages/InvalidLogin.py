from selenium import webdriver
from Tests.PageObject.Locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import test_data


class InvalidLogin:

    # Login locators
    accept_terms_button = Locator.accept_button
    sign_in_button = Locator.sign_in_button
    email_field = Locator.email_field
    next_button = Locator.next_button
    password = Locator.password
    sign_in = Locator.sign_in
    email_error_message = Locator.error_message

    def __init__(self, driver):
        self.driver = driver

    # Attempt to log in with an email address that is not registered (Invalid email)
    def click_accept_button(self):
        self.driver.find_element(By.XPATH, self.accept_terms_button).click()

    def click_sign_in_button(self):
        self.driver.find_element(By.XPATH, self.sign_in_button).click()

    def enter_email(self):
        self.driver.find_element(By.XPATH, self.email_field).clear()
        self.driver.find_element(By.XPATH, self.email_field).send_keys(test_data.invalid_username)

    def click_next_button(self):
        self.driver.find_element(By.XPATH, self.next_button).click()

    def enter_password(self):
        self.driver.find_element(By.NAME, self.password).clear()
        self.driver.find_element(By.NAME, self.password).send_keys(test_data.invalid_password)

    def click_sign_in(self):
        self.driver.find_element(By.XPATH, self.sign_in).click()


