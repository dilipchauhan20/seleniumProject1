from Practice_Proj.Locators.locators import Locators

class HomePage():

    def __init__(self,driver):
        self.driver = driver


        self.welcome_admin_link_id = Locators.welcome_admin_link_id
        self.logout_link_id = Locators.logout_link_id

    def click_wlcome_admin_link(self):
        self.driver.find_element_by_id(self.welcome_admin_link_id).click()

    def click_logout_link(self):
        self.driver.find_element_by_link_text(self.logout_link_id).click()


