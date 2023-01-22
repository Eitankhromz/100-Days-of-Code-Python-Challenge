import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


STOCK_API_KEY = 
NEWS_API_KEY = 
TICKER = "TSLA"
COMPANY_NAME = "Tesla"
account_sid = 
auth_token = 


stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={TICKER}&apikey={STOCK_API_KEY}"
response = requests.get(stock_url)
response.raise_for_status()
stock_data = response.json()

daily_data = stock_data["Time Series (Daily)"]
daily_close_list = [key for (key, value) in daily_data.items()]

current_close = daily_data[daily_close_list[0]]["4. close"]
prev_close = daily_data[daily_close_list[1]]["4. close"]

pchange = round(((float(current_close) - float(prev_close))/float(prev_close)) * 100)

up_down = None
if pchange > 0:
  up_down = "🔺"
else:
  up_down = "🔻"


if abs(pchange) > 1:

    # print("Get News")

    params = {
        "qinTitle": TICKER,
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=params)
    news_response.raise_for_status()
    news_data = news_response.json()

    articles = news_data["articles"]

    formatted_articles = [f"{TICKER}: {up_down}{abs(pchange)}%\nHeadline: {article['title']} \nBody: {article['description']}" for article in articles[:3]]
    print(formatted_articles)
    

    client = Client(account_sid, auth_token)

    for article in formatted_articles:
      message = client.messages.create(
          body=article,
          from_="+00000000000",
          to="+00000000000"
      )




