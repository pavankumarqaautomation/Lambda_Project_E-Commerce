from selenium.webdriver.common.by import By


class AccountRegistration:
    link_first_name="//*[@id='input-firstname']"
    link_last_name="//*[@id='input-lastname']"
    link_email="//*[@id='input-email']"
    link_telephone="//*[@id='input-telephone']"
    link_password="//*[@id='input-password']"
    link_confirm_password="//*[@id='input-confirm']"
    link_subscribe="//*[@id='content']/form/fieldset[3]/div/div/div[1]/label"
    check_box_agree="//*[@id='content']/form/div/div/div/label"
    button_continue_yes="//*[@id='content']/form/div/div/input"
    link_account_creation_status="//*[@id='content']/h1"

    def __init__(self,driver):
        self.driver=driver

    def first_name(self,fname):
        self.driver.find_element(By.XPATH,self.link_first_name).send_keys(fname)

    def last_name(self,lname):
        self.driver.find_element(By.XPATH,self.link_last_name).send_keys(lname)

    def email(self,email):
        self.driver.find_element(By.XPATH,self.link_email).send_keys(email)

    def telephone(self,telephone):
        self.driver.find_element(By.XPATH,self.link_telephone).send_keys(telephone)

    def password(self,password):
        self.driver.find_element(By.XPATH,self.link_password).send_keys(password)

    def confirm_password(self,confirm_password):
        self.driver.find_element(By.XPATH,self.link_confirm_password).send_keys(confirm_password)

    def subscribe(self):
        self.driver.find_element(By.XPATH,self.link_subscribe).click()

    def agree_terms_conditions(self):
        self.driver.find_element(By.XPATH,self.check_box_agree).click()

    def click_continue(self):
        self.driver.find_element(By.XPATH,self.button_continue_yes).click()

    def confirm_message(self):
        try:
            return self.driver.find_element(By.XPATH,self.link_account_creation_status).text
        except:
              None




