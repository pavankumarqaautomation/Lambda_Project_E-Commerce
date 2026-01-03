from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class HomePage():
    link_xpath_my_account="//*[@id='widget-navbar-217834']/ul/li[6]/a/div/span"
    link_xpath_login="//*[@id='widget-navbar-217834']/ul/li[6]/ul/li[1]/a"
    link_xpath_register="//*[@id='widget-navbar-217834']/ul/li[6]/ul/li[2]/a"

    def __init__(self,driver):
        self.driver=driver

    def Hover_my_account(self):
        element=self.driver.find_element(By.XPATH,self.link_xpath_my_account)
        ActionChains(self.driver).move_to_element(element).perform()

    def click_login(self):
        self.driver.find_element(By.XPATH,self.link_xpath_login).click()

    def click_register(self):
        self.driver.find_element(By.XPATH,self.link_xpath_register).click()


