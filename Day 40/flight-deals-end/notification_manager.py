import os
from twilio.rest import Client
import requests

TWILIO_SID = os.environ.get("twilio_sid")
TWILIO_AUTH_TOKEN = os.environ.get("twilio_api")
TWILIO_VIRTUAL_NUMBER = os.environ.get("twilio_phone")
TWILIO_VERIFIED_NUMBER = os.environ.get("phone")

GREEN_API = os.environ.get("whatsapp_api")
WHATSAPP_ID_INSTANCE = os.environ.get("whatsapp_id_instance")
GREEN_URL = "https://api.greenapi.com"
WHATSAPP_HEADERS = {
    'Content-Type': 'application/json'
}


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        # print(message.sid)

    def send_whatsapp(self, payload):
        endpoint = f"{GREEN_URL}/waInstance{WHATSAPP_ID_INSTANCE}/sendMessage/{GREEN_API}"
        response = requests.post(url=endpoint, headers=WHATSAPP_HEADERS, data=payload)
        print(response.status_code)
        print(response.text)
