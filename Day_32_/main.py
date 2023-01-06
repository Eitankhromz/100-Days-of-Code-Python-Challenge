##################### Extra Hard Starting Project ######################

MY_EMAIL = "test123.email1229@gmail.com"
MY_PASS = "dmbxozpyjkdlcxkk"

import pandas as pd
import datetime as dt
import smtplib
import random

# 1. Update the birthdays.csv


# 2. Check if today matches a birthday in the birthdays.csv
tdy = dt.datetime.now()
tdy_month = tdy.month
tdy_day = tdy.day
today = (tdy_month, tdy_day)


birthday_data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_data.iterrows()}

if today in birthdays_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
    #   name from birthdays.csv
    bday_person = birthdays_dict[today]
    num = random.randint(1, 3)
    file_path = f"letter_templates/letter_{num}.txt"
    with open(file_path, "r") as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", bday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #secure connection
        connection.starttls()

        #Login
        connection.login(user=MY_EMAIL, password=MY_PASS)

        #Send Message
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=bday_person["email"],
                            msg=f"Subject: Happy Birthday \n\n {contents}"
                            )



