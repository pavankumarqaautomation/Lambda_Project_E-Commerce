from selenium.webdriver.common.by import By

class LoginPage():
    email_xpath="//*[@id='input-email']"
    password_xpath="//*[@id='input-password']"
    login_button_xpath="//*[@id='content']/div/div[2]/div/div/form/input"
    Account_Login_Confirm_xpath="//*[@id='account-account']/nav/ol/li[2]"
    logout_xpath="//*[@id='column-right']/div/a[14]"
    logout_confirmation_xpath="//*[@id='content']/p[2]"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()
    def Account_Login_confirmation(self):
        try:
            return self.driver.find_element(By.XPATH,self.Account_Login_Confirm_xpath).text
        except:
            return False

