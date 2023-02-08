from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"C:\Developement\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# driver.get("https://amazon.com")
driver.get("https://www.python.org")
# driver.maximize_window()

search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))  # Search

logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)  # {'height': 72, 'width': 255}

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)  # docs.python.org

bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)  # Submit Website Bug

# ---------------------- Challenge ------------------------ #

event_month_day = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
event_dict = {}
for each in range(len(event_month_day)):
    event_dict[each] = {
        "time": f"2023-{event_month_day[each].text}",
        "event": events[each].text
    }
print(event_dict)

driver.quit()
