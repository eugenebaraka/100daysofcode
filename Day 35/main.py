import requests
from twilio.rest import Client
import os

account_sid = "AC3660c443e89f57e153472eadd6a5134f"
auth_token = os.environ.get("twilio_auth_token")

KEY = os.environ.get("weather_api_key")

ENDPOINT = "https://api.weatherapi.com/v1/forecast.json"
parameters = {
    "q": "8.980603, 38.757759",
    "key": KEY,
    "days": 1,
    "aqi": "no",
    "alerts": "no"
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

# check if it will rain in the next 12 hours
hourly_data = data["forecast"]["forecastday"][0]["hour"]

will_rain = False
for rain in hourly_data:
    conditions = rain["will_it_rain"]
    if conditions == 1:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It is going to rain today. Bring an umbrella!",
        from_='+12055780042',
        to='+15146076350'
    )

    print(message.status)



