from pageobjects.LoginPage import LoginPage
from testcases.test_001_Account_Registration import Test_001_AccountReg
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig
from pageobjects.HomePage import HomePage
import os
import pytest
from utilities.date_time_seconds import get_timestamp
from selenium.webdriver.common.by import By


class Test_Login():
    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    email= ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    def test_login(self, setup):
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.Hover_my_account()
        self.logger.info("self.hp.Hover_my_account")
        self.hp.click_login()
        self.logger.info("self.hp.click_login")

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.logger.info("self.lp.setEmail")
        self.lp.setPassword(self.password)
        self.logger.info("self.lp.setPassword")
        self.lp.clickLogin()
        self.target_page=self.lp.Account_Login_confirmation()
        self.logger.debug("self.target_page")
        if self.target_page!=False:
            assert True
            self.driver.save_screenshot(os.path.abspath(f"./screenshots/test_002_Login_Account_Pass_{get_timestamp()}.png"))
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(f"./screenshots/test_002_Login_Account_Fail_{get_timestamp()}.png"))
            self.driver.close()
            assert False