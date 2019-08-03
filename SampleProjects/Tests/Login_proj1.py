import unittest
from selenium import webdriver
import time

class Logintests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path='/Users/dilip.chauhan/Desktop/python/selenium/drivers/chromedriver 2')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.find_element_by_id('txtUsername').send_keys("Admin")
        driver.find_element_by_id('txtPassword').send_keys("admin123")
        driver.find_element_by_id('btnLogin').click()

        driver.find_element_by_id('welcome').click()
        driver.find_element_by_link_text('Logout').click()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()
