from dotenv import load
import requests
import os
from twilio.rest import Client


def configure():
    load()


STOCK_NAME = "MSFT"
COMPANY_NAME = "Microsoft Corp"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

configure()

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": os.getenv("API_STOCK_KEY")
}
stock_result = requests.get(STOCK_ENDPOINT, params=stock_params)
# print(result.json())

data = stock_result.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
# print(data_list)

previous_data = data_list[0]
closing_price_1 = previous_data["4. close"]
# print(f"${closing_price_1}")

comparing_day_before_data = data_list[1]
closing_price_2 = comparing_day_before_data["4. close"]
# print(f"${closing_price_2}")

closing_difference = float(closing_price_1) - float(closing_price_2)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
# print(closing_difference)

percent_difference = round((closing_difference / float(closing_price_1)) * 100)
# print(f"%{percent_difference}")

if abs(closing_difference):
    news_params = {
        "apiKey": os.getenv("API_NEWS_KEY"),
        "qInTitle": COMPANY_NAME,
    }
    news_result = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_result.json()["articles"]
    # print(articles)
    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down}{percent_difference}%\n" \
                          f"Headline: {article['title']}."
                          f"\nBrief: {article['description']}"
                          for article in three_articles]

    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+16506402790",
            to="+14075450511"
        )
else:
    print("No New News Today.")

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
