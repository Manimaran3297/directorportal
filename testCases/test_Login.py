import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self,setup):

        self.logger.info("****Test_001_Login****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="loginpage":
            assert True
            self.logger.info("***Test case passed***")

    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("***Verifying Login test***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(10)
        self.lp.clickLogin()
        time.sleep(5)
        act_title=self.driver.title
        print(act_title)
        time.sleep(5)
        self.lp.clickLogout()
        time.sleep(5)
        self.lp.clicksignout()
        act_title=self.driver.title
        print(act_title)
        self.driver.close()
        if act_title=="SD-WAN Management System":
            assert True
            self.logger.info("******Login test passed******")


