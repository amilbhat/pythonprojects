import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "Stock Api key from aphavantage"  # Stock api key <---

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_SID = ""             # Twilio Sid <---
TWILIO_AUTH_TOKEN = ""      # Twilio Auth Token <---

stock_parameter = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}


response = requests.get(url=STOCK_ENDPOINT, params=stock_parameter)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if diff_percent > 1:
    news_params = {
        "apikey": "News Api Key",       # News Api Key <---
        "searchIn" : "title",
        "q" : COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_article = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_="Twilio Phone number",       # <---
            to="your Phone Number"              # <---
        )







