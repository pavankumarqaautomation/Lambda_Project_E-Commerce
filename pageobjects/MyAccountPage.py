from selenium.webdriver.common.by import By


class MyAccountPage():

    logout_xpath="//*[@id='column-right']/div/a[14]"
    logout_Confirm = "//*[@id='content']/p[2]"

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(By.XPATH,self.logout_xpath ).click()

    def logout_confirmation(self):
        try:
            return self.driver.find_element(By.XPATH,self.logout_Confirm).text
        except:
            return False





 #logoutprint(logout_Confirm.text) #You have been logged off your account. It is now safe to leave the computer.