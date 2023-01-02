import smtplib

my_email = "test123.email1229@gmail.com"
password = "PUT IN YOUR OWN"

# #create an object from SMTP class
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
#
# #secure connection
# connection.starttls()
#
# #Login into from address email
# connection.login(user=my_email, password=password)
#
# #Send the email
# connection.sendmail(from_addr=my_email,
#                     to_addrs="test123.email1229@yahoo.com",
#                     msg="Subject:Hello\n\n This is the body of the email"
#                     )

#close the program
# connection.close()

#FASTER & BETTER WAY

# # create an object from SMTP class
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     #secure connection
#     connection.starttls()
#
#     #Login into from address email
#     connection.login(user=my_email, password=password)
#
#     #Send the email
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="test123.email1229@yahoo.com",
#                         msg="Subject:Hello\n\n This is the body of the email"
#                         )

import datetime as dt
import random

# #module.Class.method
# now = dt.datetime.now()
# year = now.year
# month = now.month
# week_day = now.weekday()
# print(week_day)
#
# date_of_birth = dt.datetime(year=2002, month=12, day=15)
# print(date_of_birth)

today = dt.datetime.now()

if today.weekday() == 6:
    with open("quotes.txt") as quotes_data:
        quotes = quotes_data.readlines()

        chosen_quote = random  .choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #secure connection
        connection.starttls()

        #Login
        connection.login(user=my_email, password=password)

        #Send Message
        connection.sendmail(from_addr=my_email,
                            to_addrs="test123.email1229@yahoo.com",
                            msg=f"Subject: Apologies \n\nHi Noah, \n \nIt appears I've messed up the formatting. "
                                f"However, I have (pls) fixed it now (thx). To celebrate here is a random quote "
                                f"I've scraped off the internet:\n \n"
                                f"{chosen_quote}\nFrom your boy,\nEitan"
                            )

