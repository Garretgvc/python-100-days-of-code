import smtplib
import time

import requests
from datetime import datetime

EMAIL = "christiansongg65@gmail.com"
PASSWORD = "manpvrjzuvwjkfou"

MY_LONG = -87.906471
MY_LAT = 43.038902


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        return True


def is_night():
    param = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }

    response = requests.get("http://api.sunrise-sunset.org/json", params=param)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["result"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["result"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:The ISS has arrived!\n\nThe ISS should be above your location right now."
        )
