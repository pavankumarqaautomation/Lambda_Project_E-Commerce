import time
from pageobjects.HomePage import HomePage
from pageobjects.LoginPage import LoginPage
from pageobjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen
import os
import pytest

@pytest.mark.datadriven
class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = os.path.abspath(os.curdir) + "\\testdata\\Opencart_LoginData.xlsx"

    def test_login_ddt(self, setup):
        self.logger.info("**** Starting test_003_login_Datadriven *******")

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)

        for r in range(2, self.rows + 1):

            # 🔥 Always start from Login page (NO hover)
            self.driver.get(self.baseURL + "/index.php?route=account/login")

            self.email = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            self.targetpage = self.lp.Account_Login_confirmation()

            if self.exp == 'Valid':
                if self.targetpage:
                    lst_status.append('Pass')
                    self.ma.logout()   # ✅ reset state
                else:
                    lst_status.append('Fail')

            elif self.exp == 'Invalid':
                if self.targetpage:
                    lst_status.append('Fail')
                    self.ma.logout()   # safety logout
                else:
                    lst_status.append('Pass')

        self.driver.close()

        # Final assertion
        assert "Fail" not in lst_status
        self.logger.info("******* End of test_003_login_Datadriven **********")
