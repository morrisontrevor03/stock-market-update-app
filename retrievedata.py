import requests
import datetime
import schedule
import time
import senddata
from dotenv import load_dotenv
import os

#get api key from .env
load_dotenv()
AV_key=os.getenv("AV_KEY")
print(AV_key)

#main function, gathers data from API, creates the message and calls the sms function
def stockMarketDaily():
    #exception handling for erros w/ API call
    try:
        #acquire date for indexing JSON data from API
        date = datetime.datetime.now()
        format_date = date.strftime("%Y-%m-%d")

        #get data from API
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=1&apikey=" + AV_key
        r = requests.get(url)
        data = r.json()

        #declare variables for message using data from API
        high = data['Time Series (Daily)'][format_date]['2. high']
        low = data['Time Series (Daily)'][format_date]['3. low']
        open = data['Time Series (Daily)'][format_date]['1. open']
        close = data['Time Series (Daily)'][format_date]['4. close']
        ticker = data['Meta Data']['2. Symbol']

        #create message string
        message = f"Good Evening. Here is a summary of {ticker} stock movements. AAPL opened at ${open} and closed at ${close}. It reached a high of ${high} and a low of ${low}"
        
        #call sendMessage function and pass message string as parameter
        senddata.sendMessage(message)
    except:
        message = "Error acquiring quote data"
stockMarketDaily()
#schedules stockMarketDaily() to be performed every day at 7pm system time
schedule.every().day.at("19:00").do(stockMarketDaily)

while True:
    schedule.run_pending()
    time.sleep(1)