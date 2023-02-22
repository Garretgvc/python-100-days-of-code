import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3481482005&distance=25&f_AL=true&f_E=2&geoId=105240372" \
      "&keywords=python%20developer&location=Milwaukee%2C%20Wisconsin%2C%20United%20States&refresh=true&sortBy=R "
# Only works with 2-factor authentication turned off

service = Service(r"C:\Development\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get(URL)
login = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
login.click()

username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(4)

jobs = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

for each in jobs:
    each.click()
    time.sleep(2)
    save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save.click()
    time.sleep(2)
