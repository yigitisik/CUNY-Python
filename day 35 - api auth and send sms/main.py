import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

weather_api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_api_key = os.environ.get("WEATHER_API_KEY")

twilio_account_SID = "AC39dbf92b97d034f1e78d338c150fbcaf"
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

params = {
    "lat": 43.074687,
    "lon": -89.452479,
    "appid": weather_api_key,
    "cnt": 4,
}

response = requests.get(weather_api_endpoint, params=params)
response.raise_for_status()
print(response.json())

weather_data = response.json()

expecting_Rain = False
for period_i in weather_data["list"]:
    weather_id = period_i["weather"][0]["id"]
    if int(weather_id) < 700:
        expecting_Rain = True

if expecting_Rain:
    # create Twilio client with proxy if available
    proxy_settings = {
        'http': os.environ.get('http_proxy'),
        'https': os.environ.get('https_proxy')
    }
    # Remove any None values so Twilio doesn't see them
    proxy_settings = {k: v for k, v in proxy_settings.items() if v}

    if proxy_settings:
        proxy_client = TwilioHttpClient(proxy=proxy_settings)
        twilio_client = Client(twilio_account_SID, twilio_auth_token, http_client=proxy_client)
    else:
        twilio_client = Client(twilio_account_SID, twilio_auth_token)

    message = twilio_client.messages.create(
        body= "Hi, expecting rain in next 12 hours, you may want an umbrella, ☂️",
        from_="whatsapp:+14155238886",
        to = "whatsapp:+16085145142",
    )
    message_2 = twilio_client.messages.create(
        body="Hi, expecting rain in next 12 hours, you may want an umbrella, ☂️",
        from_="whatsapp:+14155238886",
        to="whatsapp:+18572943262",
    )
    print((message.status, message.sid))
    print((message_2.status, message_2.sid))