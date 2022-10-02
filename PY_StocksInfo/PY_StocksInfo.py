import json
import requests
import os
from twilio.rest import Client


COMPANY_NAME = "Tesla"
STOCK_INTEREST = "TSLA"
STOCK_API_KEY = "API_KEY" #https://www.alphavantage.co/
STOCK_WEBSITE = "https://www.alphavantage.co/query"
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_INTEREST,
    "apikey": STOCK_API_KEY
}

NEWS_API = "API_KEY" #https://newsapi.org/
NEWS_WEBSITE = "https://newsapi.org/v2/everything"


#def get_prev_day(previous_day:str)->int:
#    start_index = previous_day.rfind("-") + 1
#    end_index = previous_day.find(" ")
#    get_number = previous_day[start_index:end_index]
#    prev_day = str(int(get_number) - 1)
#    new_date = previous_day.replace(get_number, prev_day)
#    return new_date


def percent_diff(old_value:float, new_value:float)->float:
    difference = (new_value*100)/old_value
    return round(difference - 100, 2)

def send_message():
    global NEWS_WEBSITE
    client = Client(account_sid, auth_token)
    news_params = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "language": "en",
        "apiKey": NEWS_API,
        "from": previous_day,
        "to": day_before,
        "sortBy": "popularity"
    }
    news_response = requests.get(NEWS_WEBSITE, news_params)
    news_data = news_response.json()
    most_popular_news = news_data["articles"][:3]
    message = client.messages.create(
                            body=f"\nTesla Stock Prices:\nLatest value: {latest_value}, Day before value: {old_value}\nDifference: {value_difference}, {percent_difference}%",
                            from_='+NUMBER',
                            to='+NUMBER'
                    )
    print(most_popular_news)
    for news in most_popular_news:
        message = client.messages.create(
                            body=f"\nHeadline: {news['title']}\nContent: {news['description']}\nLink: {news['url']}",
                            from_='+NUMBER',
                            to='+NUMBER'
                    )    

account_sid = os.environ['TWILIO_ACCOUNT_SID'] = "API_KEY"
auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'API_KEY'
os.environ["ACC_KEY"] = "API_KEY"


stock_response = requests.get(STOCK_WEBSITE, STOCK_PARAMS)
stock_response.raise_for_status()
data = stock_response.json()

days_in_data = list(data["Time Series (Daily)"].keys())

previous_day = data["Time Series (Daily)"][days_in_data[0]]
latest_value = float(previous_day["4. close"])

day_before = data["Time Series (Daily)"][days_in_data[1]]
old_value = float(day_before["4. close"])

value_difference = round(latest_value - old_value, 2)
percent_difference = percent_diff(old_value, latest_value)

if percent_difference > 5 or percent_difference < -5:
    send_message()