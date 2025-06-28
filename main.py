import requests
import random
from twilio.rest import Client
import datetime as dt

try:
    response = requests.get("http://127.0.0.1:5000/api/love-quotes")
    response.raise_for_status()
    quotes = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching quotes: {e}")

quotes = quotes["love_quotes"]
quote = random.choice(quotes)


def show_daily():
    hour = dt.datetime.now().hour
    minute = dt.datetime.now().minute

    if hour == 7 and minute == 00:
        client = Client(account_sid, auth_token)
        try:
            message = client.messages.create(
                from_="whatsapp:+14155238886",
                body=f"{quote}",
                to="whatsapp:+2348153857254",
            )
            print(message.status)
        except Exception as e:
            print(f"Error sending message: {e}")


show_daily()
