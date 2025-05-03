import requests
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
key1_stock_prices = os.getenv("Stock_api")
key2_news = os.getenv("News_api")

STOCK_NAME = "RELIANCE.BSE"
COMPANY_NAME = 'RELI'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://api.marketaux.com/v1/news/all"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": key1_stock_prices,
}
news_params ={
    "symbols":COMPANY_NAME,
    'filter_entities':'true',
    "language":'en',
    "api_token": key2_news
}
articles={}
#sending request for stock prices and getting yesterday and previous day closing day prices
def fetch_articles():
    value_e = 0
    for i in range(3):
        news_ict = news_data.get('data')[i]
        for (key, value) in news_ict.items():
            if key == 'title':
                title_key = value
                articles[title_key] = value_e
            elif key == "url":
                value_e = value
                articles[title_key] = value_e

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
previous_day_data = data_list[1]
previous_day_closing_price = previous_day_data["4. close"]

# print(yesterday_closing_price)
# print(previous_day_closing_price)

# difference between stock prices
up_down = None
difference = float(yesterday_closing_price) - float(previous_day_closing_price)
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

if abs(diff_percent) > 0.5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()
    fetch_articles()
    print(articles)