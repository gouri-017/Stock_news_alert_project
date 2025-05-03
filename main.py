import requests
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
key1_stock_prices = os.getenv("Stock_api")
key2_news = os.getenv("News_api")