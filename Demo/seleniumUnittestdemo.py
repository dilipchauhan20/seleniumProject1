import unittest
from selenium import webdriver
import HtmlTestRunner

class MyTestCase(unittest.TestCase):


    # def test_something(self):
    #     self.assertEqual(True, False)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver 2")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # def setUp(self):
    #     self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver 2")
    #     self.driver.implicitly_wait(10)
    #     self.driver.maximize_window()

    def test_search1(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step step")
        self.driver.find_element_by_name('btnK').click()
        x = self.driver.title
        print(x)
        self.assertEqual(x,"Automation step step - Google Search")

    def test_search2(self):
        self.driver.implicitly_wait(20)
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("a1 technology")
        self.driver.find_element_by_name('btnK').click()
        x = self.driver.title
        print(x)
        self.assertEqual(x,"a1 technology - Google Search")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """

    # def tearDown(self):
    #     self.driver.close()
    #     self.driver.quit()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dilip.chauhan/Desktop/python/selenium/Reports'), verbosity=2)
