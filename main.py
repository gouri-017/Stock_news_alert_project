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
