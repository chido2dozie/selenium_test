import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Tests.PageObject.Locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import test_data


class LoginPage:

    # Login locators
    accept_terms_button = Locator.accept_button
    sign_in_button = Locator.sign_in_button
    email_field = Locator.email_field
    next_button = Locator.next_button
    password = Locator.password
    sign_in = Locator.sign_in
    logout = Locator.logout_button
    user_profile = Locator.profile

    def __init__(self, driver):
        self.driver = driver

    # Sign in to account
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

    # Expand user profile button to display options and verify that Sign out button is present
    def check_logout_button(self):
        user = self.driver.find_element(By.XPATH, self.user_profile)
        a_chains = ActionChains(self.driver)
        a_chains.move_to_element(user).perform()
        sleep(2)
        log_out = self.driver.find_element(By.XPATH, self.logout)
        return log_out


