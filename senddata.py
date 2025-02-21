import requests
from dotenv import load_dotenv
import os

#get protected data from .env
load_dotenv()

phone=os.getenv("phone")
key=os.getenv("TB_key")

#sends the text message using the message string from stockMarketDaily()
def sendMessage(message):
    #sends required data to textbelt API
    response = requests.post('https://textbelt.com/text',{
        'phone': phone,
        'message': message,
        'key': key
    })
    print(response.json())