import requests
from twilio.rest import Client
import os
import datetime as dt

STOCK_NAME = "TLRY"
COMPANY_NAME = "Tilray Brands, Inc."

today = dt.datetime.today()
yesterday_date = today - dt.timedelta(days=0)
yesterday_date = yesterday_date.strftime('%Y-%m-%d')

before_yesterday_date = today - dt.timedelta(days=1)
before_yesterday_date = before_yesterday_date.strftime('%Y-%m-%d')


# SET UP APIs
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("stock_api_key")
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("news_api_key")
news_params = {
    "apiKey": NEWS_API_KEY,
    "q": f"{COMPANY_NAME} AND {STOCK_NAME}",
    "searchIn": "title,description",
    "from": before_yesterday_date,
    "to": yesterday_date,
    "language": "en",
    "sortBy": "popularity"
}

TWILIO_ACC_SID = "AC3660c443e89f57e153472eadd6a5134f"
TWILIO_AUTH_TOKEN = os.environ.get("twilio_auth_token")

# Call the API to extract stock prices
stock_price_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
print(stock_price_response.status_code)
stock_prices = stock_price_response.json()["Time Series (Daily)"]

# get yesterday's closing price

two_day_closes = {k: v['4. close'] for (k, v) in stock_prices.items()
                  if k in (before_yesterday_date, yesterday_date)}

prices_list = list(two_day_closes.values())
prct_change = (abs(float(prices_list[0]) - float(prices_list[1])) / float(prices_list[0])) * 100


if prct_change > 5:  # specify the percentage change for getting the news

    # call API to get news about company
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    print(news_response.status_code)

    news_data = news_response.json()["articles"]
    popular_articles = news_data[:3]

    message_body = None

    for article in popular_articles:
        title = article["title"]
        descr = article["description"]
        url = article["url"]

        if float(prices_list[0]) > float(prices_list[1]):
            message_body = f"{STOCK_NAME}: 🔺{int(prct_change)}%\nHeadline: {title}\nBrief: {descr}\n{url}"
            # print(message_body)
        else:
            message_body = f"{STOCK_NAME}: 🔻{int(prct_change)}%\nHeadline: {title}\nBrief: {descr}\n{url}"
            # print(message_body)

        client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            body=message_body,
            from_='+12055780042',
            to=os.environ.get("phone_num")
        )

        print(message.status)
