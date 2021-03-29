

class LoginPage:
    textbox_username_id="username"
    textbox_password_id="password"
    button_login_xpath="//*[@id='loginForm']/div[4]/button"
    button_logout_xpath="//*[@id='dropdownMenu1']/span"
    button_signout_xpath="//*[@id='top_right']/li[4]/ul/li[3]/a"


    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()

    def clicksignout(self):
        self.driver.find_element_by_xpath(self.button_signout_xpath).click()
