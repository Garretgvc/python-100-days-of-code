import requests
import os
from twilio.rest import Client

account_sid = "Twillo SID here"
auth_token = "Twillo Token here"
OMW_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "Enter Open Weather API Key Here"

weather_params = {
    "lat": 43.038902,
    "lon": -87.906471,
    "appid": api_key
}

will_it_rain = False

response = requests.get(OMW_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:4]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_it_rain = True

if will_it_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It's going to rain/snow today. Remember to bring a Umbrella",
            from_='+16506402790',
            to='+14075450511')

else:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It's going to a clear day today.",
            from_='+16506402790',
            to='+14075450511')

print(message.status)
