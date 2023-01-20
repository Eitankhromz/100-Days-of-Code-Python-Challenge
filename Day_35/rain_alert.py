import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Set environment variables for your credentials

account_sid = "AC5432c6013c9357353acab478bdd867f0"
api_key = os.environ.get("OWM_APi_KEY")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 39.815827,
    "lon": -74.451292,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

# create a response object to call request
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
# print(response)

# raise exceptions
response.raise_for_status()

# create a variable equal to the JSON
weather_data = response.json()


will_rain = False
hour = weather_data["hourly"][:12]

for key in hour:
    weather_id = key["weather"][0]["id"]

    if int(weather_id) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hello, friendly reminder that it is going to rain today",
        from_="0000000000",
        to="+0000000000"
    )

    print(message.status)

