from POMdemo.Locators.locators import Locators

class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.welcome_link_id = Locators.welcome_link_id
        self.logout_linktext = Locators.logout_linktext

    def click_welcome(self):
        self.driver.find_element_by_id(Locators.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(Locators.logout_linktext).click()