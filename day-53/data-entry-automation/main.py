from bs4 import BeautifulSoup
import requests
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Link to google forms
GOOGLE_FORMS = "https://docs.google.com/forms/d/e/1FAIpQLScxzzc4vRcsqLt3NUwTCOkW3BDPYQmG9CxQmAtKlfM9nAnj1w/viewform" \
       "?usp=sf_link"
URL = "https://www.zillow.com/orlando-fl/rentals/?searchQueryState=%7B%22pagination%22%3A       %7B%7D%2C" \
      "%22usersSearchTerm%22%3A%22Orlando%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.71192942651224" \
      "%2C%22east%22%3A-80.90855418237162%2C%22south%22%3A28.261878481913694%2C%22north%22%3A28" \
      ".77109605698259%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A13121%2C%22regionType%22%3A6%7D%5D" \
      "%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22" \
      "%3A398175%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A2000%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C" \
      "%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B" \
      "%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse" \
      "%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B" \
      "%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D "
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/109.0.0.0 Safari/537.36 "
ZILLOW_MP = "https://www.zillow.com/"

# collect webpage data
response = requests.get(URL, headers={
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT})
zillow_data = response.content

# scrape information for rental properties
soup = BeautifulSoup(zillow_data, "html.parser")
json_data = soup.findAll("script", attrs={"type": "application/json"})
rent_data = json_data[1].text
rent_data = rent_data.replace("<!--", "")
rent_data = rent_data.replace("-->", "")
rent_data = json.loads(rent_data)
# print(len(rent_data["cat1"]["searchResults"]["listResults"]))   # 40 rentals detected

# save targeted information into lists
listings = []
prices = []
addresses = []
for each in rent_data["cat1"]["searchResults"]["listResults"]:
    # save all listings
    if ZILLOW_MP not in each["detailUrl"]:
        listings.append(ZILLOW_MP + each["detailUrl"])
    else:
        listings.append(each["detailUrl"])
    # save all addresses
    addresses.append(each["address"])
    # save all prices
    try:
        prices.append(each["price"])
    except KeyError:
        prices.append(each["units"][0]["price"])

options = webdriver.ChromeOptions()
service = Service(r"C:\Development\chromedriver.exe")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
print(len(listings))


# load information into google forms
def import_info():
    for listing in range(len(listings)):
        driver.get(GOOGLE_FORMS)
        time.sleep(1)

        address_input = driver.find_element(By.XPATH,
                                            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(addresses[listing])

        price_input = driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(prices[listing])

        listing_input = driver.find_element(By.XPATH,
                                            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        listing_input.send_keys(listings[listing])

        submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit.click()
        time.sleep(1)

        if listing < len(listings):
            another_form = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_form.click()
    driver.quit()


import_info()
