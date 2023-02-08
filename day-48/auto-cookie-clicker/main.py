from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(r"C:\Development\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

time_frame = time.time() + 1

# Set end_time to 5 minutes in the future
end_time = time.time() + 60 * 5

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "coolie")

# Use CSS_Selector to "drill-down" into the store id to get the divs inside
all_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = []

for each in all_items:
    item_ids.append(each.get_attribute("id"))

while True:
    cookie.click()

    if time.time() > time_frame:
        buyable = []
        store = driver.find_element(By.CSS_SELECTOR, "#store div")
        # Start at the most expensive item and work your way down
        for each in store[:-1]:
            if each.get_attribute("class") != "grayed":
                buyable.append(each)
        buyable[-1].click()
        time_frame = time.time() + 5

    if time.time() > end_time:
        cookies_to_print = driver.find_element(By.ID, "cps").text
        print(cookies_to_print)
        break
