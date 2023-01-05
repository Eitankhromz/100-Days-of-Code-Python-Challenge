import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 0000
MY_LONG = 0000
MY_EMAIL = "test123.email1229@gmail.com"
MY_PASS = "YOUR OWN"


def see_iss():
    """Checks to see if ISS location is within range (+/- 5 degrees) and returns True or False"""
    global MY_LAT, MY_LONG
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    # Raises Exception Errors
    response.raise_for_status()

    # Retrieving JSON data
    data = response.json()  # imports JSON data as a dictionary so can tap into any key i.e [iss_position]
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if iss_latitude in range(round(MY_LAT - 5), round(MY_LAT + 5)) and iss_longitude in range(round(MY_LONG - 5),
                                                                                              round(MY_LONG + 5)):
        return True


def is_night():
    """Checks if it is nighttime and returns True if it is and False if it is not"""
    parameters = {
        "lat": None,
        "lng": None,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # print(sunrise)
    # print(sunset)

    time_now = datetime.now()
    current_hour = time_now.hour

    if current_hour > sunset or current_hour < sunrise:
        return True

while True:
    time.sleep(60)
    if see_iss() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            #secure connection
            connection.starttls()

            #Login
            connection.login(user=MY_EMAIL, password=MY_PASS)

            #Send Message
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="test123.email1229@yahoo.com",
                                msg=f"Subject: ISS is above you \n\n Hey, \n\n Look up! The ISS is righ above you. Can you "
                                    f"see it?"
                                )


