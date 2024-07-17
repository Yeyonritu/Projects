import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

interval = '60min'
symbol = STOCK
api_key = "NO5MDZH9EW8W7BQW"
month = "2024-07"

news_api_key = "d155318aa8d441e0a1b7d835901a9c85"

stock_parameters = {
    "function":'TIME_SERIES_INTRADAY',
    "symbol": symbol,
    "interval": interval,
    "apikey": api_key,
    "month": month,
}

news_parameters = {
    "q":COMPANY_NAME,
    "apikey":news_api_key,
}

my_email = "gvic0302@gmail.com"
password = "nqjhuyepukchgbru"

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()
tday_closing = float(data["Time Series (60min)"]["2024-07-16 19:00:00"]["4. close"])
yday_closing = float(data["Time Series (60min)"]["2024-07-15 19:00:00"]["4. close"])

# diff_percent = (5/100) * yday_closing
diff_percent = abs(tday_closing - yday_closing) / yday_closing * 100

news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

# if yday_closing in range(int(tday_closing-diff_percent), int(tday_closing + diff_percent)):
if diff_percent >= 5 or diff_percent <= 5:
    for i in range(3):
        articles = news_data["articles"][i]
        title = articles["title"]
        message = articles["content"]

        content = f"Subject: TESLA UPDATE \n\n{title}\n{message}"
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="myvp18@gmail.com", msg=content.encode('utf-8'))
        
else:
    print("Price change is less than 5%. No news fetched.")