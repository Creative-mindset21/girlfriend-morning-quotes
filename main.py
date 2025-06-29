import requests, random, datetime as dt, os
from twilio.rest import Client
from dotenv import load_dotenv
from data import *

load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

emoji = random.choice(love_emojis)
name = random.choice(sweet_names)

try:
    response = requests.get("https://bd1b-138-250-191-248.ngrok-free.app/")
    response.raise_for_status()
    quotes = response.json()
    quotes = quotes["love_quotes"]
    quote = random.choice(quotes)
except requests.exceptions.RequestException as e:
    print(f"Error fetching quotes: {e}")


def show_daily():
    hour = dt.datetime.now().hour
    minute = dt.datetime.now().minute

    if hour == 4 and minute == 00:
        client = Client(account_sid, auth_token)
        try:
            message = client.messages.create(
                from_="whatsapp:+14155238886",
                body=f"Hey {name}{emoji}\n\n{quote}\n\nI hope this made you smile my love {emoji}",
                to="whatsapp:+2348144613052",
            )
            print(message.status)
        except Exception as e:
            print(f"Error sending message: {e}")


show_daily()
