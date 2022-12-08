__author__ = 'Chidozie Amefule'


class Locator(object):

    # Login locators
    accept_button = "//div[@class='actions couple']//button[@name='agree']"
    sign_in_button = "//div[@id='ybarAccountProfile']//a"
    email_field = "//input[@id='login-username']"
    next_button = "//input[@id='login-signin']"
    password = "password"
    sign_in = "//div[@class='button-container']//button"
    profile = "//span[normalize-space()='123']"
    logout_button = "//span[normalize-space()='Sign out']"
    error_message = "//p[@class='error-msg']"

    # Home page locators
    finance_button = "//div[@id='ybar']//a[contains(text(),'Finance')]"
    market_data_button = "//div[contains(text(),'Market Data')]"
    calendar_button = "//li//ul//a[@title='Calendar']"
    next = "//a[@title='Next']"
    events = "//div[@id='fin-cal-events']//ul//li[2]//span[normalize-space()='Earnings']"
