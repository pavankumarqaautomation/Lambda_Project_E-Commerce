from utilities.randomestring import *
from pageobjects.AccountRegistration import AccountRegistration
from pageobjects.HomePage import HomePage
import os
from utilities.date_time_seconds import get_timestamp
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen
import pytest

class Test_001_AccountReg:
    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self, setup):
        #self.logger = LogGen()
        self.logger.info("***Test_001_AccountReg Started***")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("***Test_001_AccountReg Maximize window***")

        self.hp=HomePage(self.driver)
        self.hp.Hover_my_account()
        self.logger.info("***Test_001_AccountReg Hover My Account***")
        self.hp.click_register()

        self.regpage=AccountRegistration(self.driver)
        self.email = random_email()
        self.logger.info("***Test_001_AccountReg Email***")
        self.mobile = random_mobile_number()
        self.password = random_password()
        self.first_name = random_first_name()
        self.last_name = random_last_name()
        self.regpage.first_name(self.first_name)
        self.regpage.last_name(self.last_name)
        #self.regpage.email("iwuewri@gmail.com")
        self.regpage.email(self.email)
        self.regpage.telephone(self.mobile)
        self.regpage.password(self.password)
        self.regpage.confirm_password(self.password)
        self.regpage.subscribe()
        self.regpage.agree_terms_conditions()
        self.regpage.click_continue()
        self.confmsg=self.regpage.confirm_message()
        if self.confmsg=="Your Account Has Been Created!":
            assert True
            self.driver.save_screenshot(os.path.abspath(f"./screenshots/test_001_Account_Register_Pass_{get_timestamp()}.png"))
            self.logger.info("***Test_001_AccountReg Ended***")
            #self.driver.save_screenshot(os.path.abspath("./screenshots/test_001_Account_Register.png"))
            self.driver.close()
        else:
            #self.driver.save_screenshot(f"screenshots/login_{get_timestamp()}.png")
            self.driver.save_screenshot(os.path.abspath(f"./screenshots/test_001_Account_Register_Fail_{get_timestamp()}.png"))
            self.logger.error("***Test_001_AccountReg Failed***")
            self.driver.close()
            assert False
        self.logger.info("***Test_001_AccountReg Ended***")


