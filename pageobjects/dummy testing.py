from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='input-email']").send_keys("saljfdlsajfl@gmail.com")
driver.find_element(By.XPATH,"//*[@id='input-password']").send_keys("L2Z7ri!Hw6rcLfb")
driver.find_element(By.XPATH,"//*[@id='content']/div/div[2]/div/div/form/input").click()
account=driver.find_element(By.XPATH,"//*[@id='content']/div[1]/h2")
print(account.text)  #My Account
driver.find_element(By.XPATH,"//*[@id='column-right']/div/a[14]").click() #logout
logout_Confirm=driver.find_element(By.XPATH,"//*[@id='content']/p[2]")
print(logout_Confirm.text) #You have been logged off your account. It is now safe to leave the computer.