from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(r"C:\Development\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# english_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
# print(english_articles)

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# ------------------- Challenge ---------------------- #

driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Garyam")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Chrisriguez")

email = driver.find_element(By.NAME, "email")
email.send_keys("christiansongg@yahoo.com")

# submit = driver.find_element(By.CLASS_NAME, "btn")
# submit.send_keys(Keys.ENTER)

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
