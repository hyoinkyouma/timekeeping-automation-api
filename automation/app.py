from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

isDev:bool = True

#init webdriver
def initWebDriver ():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def clickBtn(email:str, password:str) -> bool:
    driver = initWebDriver()
    def login(email:str, password:str) -> bool:
        driver.get("https://app.salarium.com/users/login")
        driver.implicitly_wait(10)
        elems = driver.find_elements(By.CLASS_NAME,"form-control")
        btn = driver.find_element(By.CLASS_NAME, "btn-form-custom")
        elems[0].send_keys(email)
        elems[1].send_keys(password)
        btn.click()
        isPresent:bool
        try:
            driver.find_element(By.CLASS_NAME,"alert-danger")
            isPresent = True
        except:
            isPresent = False
        return not isPresent

    didLogin = login(email, password)
    if didLogin:
        btn = driver.find_element(By.ID, "time_btn")
        btn.click()
        return True
    else:
        return False

