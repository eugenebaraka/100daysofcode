from twilio.rest import Client
import os
import requests

# access twilio
TWILIO_ACC_SID = "AC3660c443e89f57e153472eadd6a5134f"
TWILIO_AUTH_TOKEN = os.environ.get("twilio_auth_token")
# to access whatsapp
GREEN_API = os.environ.get("whatsaap_api")
WHATSAPP_CHAT_ID = os.environ.get("whatsapp_chatid")
WHATSAPP_ID_INSTANCE = os.environ.get("whatsapp_id_instance")
GREEN_URL = "https://api.greenapi.com"
WHATSAPP_HEADERS = {
    'Content-Type': 'application/json'
}


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, kiwi_search_body: dict):
        self.kiwi_search_body = kiwi_search_body

    def send_message(self, to_city: str, to_iata: str, cheapest_flight: dict, whatsapp: bool = False):

        currency = self.kiwi_search_body["curr"]
        from_city = self.kiwi_search_body["fly_from"]

        new_price = cheapest_flight["new_price"]
        from_date = cheapest_flight["from_date"]
        to_date = cheapest_flight["to_date"]
        nights = cheapest_flight["nights"]
        link = cheapest_flight["link"]

        message = f"TravelBot: Only ${new_price}{currency} to fly from {from_city} to {to_city}-{to_iata}, " \
                  f"from {from_date} to {to_date} for {nights} nights! {link}"

        if whatsapp:
            payload = f"{{\r\n\t\"chatId\": \"{WHATSAPP_CHAT_ID}\",\r\n\t\"message\": " \
                      f"\"{message}\"\r\n}}"
            self.whatsapp_message(payload=payload)


        else:
            self.imessage(message_body=message)

    def imessage(self, message_body):
        client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message_body,
            from_='+12055780042',
            to=os.environ.get("phone_num")
        )

        print(message.status)

    def whatsapp_message(self, payload):
        endpoint = f"{GREEN_URL}/waInstance{WHATSAPP_ID_INSTANCE}/sendMessage/{GREEN_API}"
        response = requests.post(url=endpoint, headers=WHATSAPP_HEADERS, data=payload)
        print(response.status_code)
        print(response.text)
