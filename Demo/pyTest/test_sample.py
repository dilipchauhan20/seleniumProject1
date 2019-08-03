from selenium import webdriver
import pytest


class Test_sample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path='/Users/dilip.chauhan/Desktop/python/selenium/drivers/chromedriver 2')
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_Login(self,test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        x = driver.title
        assert x == "OrangeHRM"

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test completed")