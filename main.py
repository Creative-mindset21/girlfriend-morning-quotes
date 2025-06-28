import requests
import random

try:
    response = requests.get("http://127.0.0.1:5000/api/love-quotes")
    response.raise_for_status()
    quotes = response.json()
    quotes = quotes["love_quotes"]

    quote = random.choice(quotes)


except requests.exceptions.RequestException as e:
    print(f"Error fetching quotes: {e}")
