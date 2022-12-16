from encodings import utf_8
import os
from selenium import webdriver

os.environ['PATH'] += "D:\BrowserAutomation\msedgedriver.exe"

# going to login to linked

options = webdriver.EdgeOptions()
options.add_argument("--ignore-certificate-errors")
# options.add_argument("--incognito")
# options.add_argument("--headless")

driver = webdriver.Edge(options = options)

driver.get("https://www.linkedin.com/")

driver.implicitly_wait(30)

"""
Now going to enter text in text field for login
"""

# to use by import
from selenium.webdriver.common.by import By

username = driver.find_element(By.ID, 'session_key') # -> you need to find these elements by inspecting the website
password = driver.find_element(By.ID, 'session_password')
''' above we got the text fields, now we need to populate them '''
# syntax, = object.send_keys("text")
username.send_keys("ashish1qwerty1@gmail.com")
password.send_keys("1Lovepubg.")



# after filling the 
button = driver.find_element("xpath", '//*[@id="main-content"]/section[1]/div/div/form/button')
button.click()


profile = driver.find_element("xpath", "/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div[1]/div[1]/a/div[2]")
profile.click()

import time
time.sleep(5)

# proflePhoto = driver.find_element(By.XPATH, '//*[@id="ember167"]')
# proflePhoto.click()




page_source_ = driver.page_source

from bs4 import BeautifulSoup
import lxml

soup = BeautifulSoup(page_source_, 'lxml')
print(soup.prettify())
views = soup.find("section", id = "ember585")
print(views)


# from pprint import pprint
# pprint(page_source_)



# with open("source.html", 'wb') as f:
#     f.write(page_source_)
#     f.close()


"""
This is for closing the browser after the work is done
"""
# import time

# time.sleep(10)

# driver.close()