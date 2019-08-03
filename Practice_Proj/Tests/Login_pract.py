from selenium import webdriver
import time
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Practice_Proj.Pages.HomePage import HomePage
from Practice_Proj.Pages.LoginPage import LoginPage


class Login_Pract(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/Users/dilip.chauhan/Desktop/python/selenium/drivers/chromedriver 2')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)


    def test_login(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_loginbtn()
        # self.driver.find_element_by_id('txtUsername').send_keys("Admin")
        # self.driver.find_element_by_id('txtPassword').send_keys("admin123")
        # self.driver.find_element_by_id('btnLogin').click()
        print("click on Login")

    def test_logout(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_wlcome_admin_link()
        homepage.click_logout_link()

        # self.driver.find_element_by_id('welcome').click()
        # self.driver.find_element_by_link_text('Logout').click()
        print("Click on Logout")
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dilip.chauhan/Desktop/python/selenium/Reports'))
