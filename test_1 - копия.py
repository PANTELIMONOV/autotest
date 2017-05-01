from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class Find_Form_Auth():
    def form(self):
        baseURL="http://the-internet.herokuapp.com/"
        login="tomsmith"
        password="SuperSecretPassword!"
        driverLocation = "C:\\Users\\pantelimonov.m\\workspace\\libs\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseURL)

        elmentByXpath = driver.find_element(By.XPATH, "//a[@href='/login']")
        elmentByXpath.click()
        login_field = driver.find_element(By.ID,"username").send_keys(login)
        password_field = driver.find_element(By.ID,"password").send_keys(password)
        login_key = driver.find_element(By.XPATH,"//button[@class='radius']")
        login_key.click()
        driver.save_screenshot('screenie.png')
        driver.quit()




test = Find_Form_Auth()
test.form()