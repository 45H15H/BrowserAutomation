# required imports
from selenium import webdriver # -> webdriver
from selenium.webdriver.common.by import By # -> for using ID, XPATH, CSS etc to select elements
import os # -> os for Add to PATH

# we need to add the specific webdriver to the PATH
os.environ['PATH'] += "D:\BrowserAutomation\msedgedriver.exe"

# start webdriver instance
driver = webdriver.Edge()

import time

# going to this website
driver.get("https://www.saucedemo.com/")
time.sleep(5)
# finding login space
# userName = driver.find_element("xpath", '//*[@id="user-name"]')
# passWord = driver.find_element("xpath", '//*[@id="password"]')


# finding the username and password on the page
user = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div[1]/text()[2]')


print(user.text)
time.sleep(4)

driver.close()