import smtplib

FROM_EMAIL = "place email here"
TO_EMAIL = "place recieving email here"
PASSWORD = "make password"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(from_addr=email,
#                         to_addrs="christiansongg@yahoo.com",
#                         msg="Subject:This is my first sent email.\n\nBody paragraph.")

import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        # saves all quotes to a list
        all_quotes = quote_file.readlines()
        quote_of_the_day = random.choice(all_quotes)

    print(quote_of_the_day)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=FROM_EMAIL,
            msg=f"Subject:Monday Motivational Quote\n\n{quote_of_the_day}"
        )




