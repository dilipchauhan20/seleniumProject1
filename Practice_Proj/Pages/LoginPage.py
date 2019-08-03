from Practice_Proj.Locators.locators import Locators

class LoginPage():


    def __init__(self,driver):
        self.driver = driver

        self.username_textboxid = Locators.username_textboxid
        self.password_textboxid = Locators.password_textboxid
        self.login_buttonid = Locators.login_buttonid

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textboxid).clear()
        self.driver.find_element_by_id(self.username_textboxid).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textboxid).clear()
        self.driver.find_element_by_id(self.password_textboxid).send_keys(password)
    def click_loginbtn(self):
        self.driver.find_element_by_id(self.login_buttonid).click()


