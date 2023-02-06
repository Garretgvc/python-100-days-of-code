import requests
from bs4 import BeautifulSoup
import smtplib
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
TARGET_PRICE = 60.00

URL = "https://www.amazon.com/Mi-Computer-Monitor-Light-Bar/dp/B08W2C5W59/ref=sr_1_3?crid=16XA0JVH8XPJG&keywords" \
      "=xiaomi+monitor+light+bar&qid=1675716697&sprefix=Xiaomi+%2Caps%2C113&sr=8-3 "
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/109.0.0.0 Safari/537.36 "

response = requests.get(URL,
                        headers={"Accept-Language": ACCEPT_LANGUAGE,
                                 "User-Agent": USER_AGENT})
# print(response.status_code)

Amazon_data = response.content
soup = BeautifulSoup(Amazon_data, "html.parser")
# print(soup.prettify())

price_tag = soup.find(name="span", class_="a-offscreen")
price = float(price_tag.get_text().strip("$"))
# print(price)

item_tag = soup.find(name="span", id="productTitle")
item_name = item_tag.get_text().strip("  ")
# print(item_name)

if price <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n"
                f"{item_name}\n"
                f"is now {price}.\n\n"
                f"{URL}"
        )
