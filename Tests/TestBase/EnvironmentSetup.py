import unittest
import datetime
from selenium import webdriver
from Drivers.drivers import driver_service


class EnvironmentSetup(unittest.TestCase):

    # Setup contains the browser setup attribute
    def setUp(self):
        self.driver = webdriver.Chrome(service=driver_service)
        self.driver.maximize_window()
        self.driver.get("https://uk.yahoo.com/")
        print("Run started at: " + str(datetime.datetime.now()))
        print("Environment Set Up")
        print("----------")
        self.driver.implicitly_wait(10)

    # Teardown method to close all browser instances
    def tearDown(self):
        print("----------")
        print("Test Environment Destroyed")
        print("Run completed at: " + str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

