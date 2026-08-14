from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os
from dotenv import load_dotenv
load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

    def send_whatsapp(self, body):
        message_2 = self.client.messages.create(
            body=body,
            from_=f"whatsapp:{os.getenv("TWILIO_FROM_NUMBER")}",
            to=f"whatsapp:{os.getenv("TWILIO_TO_NUMBER")}",
        )
        print((message_2.status, message_2.sid))