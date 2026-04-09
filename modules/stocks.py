import requests
import os
from dotenv import load_dotenv
from core.speak import speak

load_dotenv()

API_KEY = os.getenv("STOCK_API_KEY")

def get_stock(symbol):
    try:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        
        response = requests.get(url)
        data = response.json()

        price = data.get("Global Quote", {}).get("05. price", None)

        if price:
            speak(f"The current price of {symbol} is {price} dollars")
        else:
            speak("Sorry, I couldn't fetch the stock price")

    except Exception as e:
        print("Stock error:", e)
        speak("Error fetching stock data")