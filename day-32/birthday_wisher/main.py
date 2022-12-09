import smtplib
from datetime import datetime
import pandas
import random

EMAIL = "christiansongg65@gmail.com"
PASSWORD = "manpvrjzuvwjkfou"

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays:
    person = birthdays[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=person["email"],
            msg=f"Subject: Happy Birthday!!\n\n{contents}"
        )
