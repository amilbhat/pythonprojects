#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

# visit https://www.twilio.com/ and create a free account to obtain auth token and account sid and virtual phone number
# visit https://openweathermap.org/ and create a free account to obtain the api key
# Also make sure you have installed necessary libraries

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")         # Open weather api here <-
account_sid = "YOUR ACCOUNT SID"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": "YOUR LATITUDE",                 # Your latitude
    "lon": "YOUR LONGITUDE",                # Your longitude
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",                 # YOUR TWILIO VIRTUAL NUMBER
        to="YOUR TWILIO VERIFIED REAL NUMBER"               # YOUR TWILIO VERIFIED REAL NUMBER
    )
    print(message.status)
