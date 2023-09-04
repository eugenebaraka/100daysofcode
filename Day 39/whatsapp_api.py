import os
import requests

GREEN_API = os.environ.get("whatsaap_api")
WHATSAPP_CHAT_ID = os.environ.get("whatsapp_chatid")
WHATSAPP_ID_INSTANCE = os.environ.get("whatsapp_id_instance")
GREEN_URL = "https://api.greenapi.com"
WHATSAPP_HEADERS = {
    'Content-Type': 'application/json'
}

test_message = "TravelBot:Only $158CAD to fly from Ottawa-YOW to Vancouver-, from 2023-10-18 to 2023-10-25 for 7 nights!" \
          " http://tinyurl.com/2bfjsuns"

payload = f"{{\r\n\t\"chatId\": \"{WHATSAPP_CHAT_ID}\",\r\n\t\"message\": " \
          f"\"{test_message}\"\r\n}}"

def whatsapp_message(payload):
    endpoint = f"{GREEN_URL}/waInstance{WHATSAPP_ID_INSTANCE}/sendMessage/{GREEN_API}"
    response = requests.post(url=endpoint, headers=WHATSAPP_HEADERS, data=payload)
    print(response.status_code)
    print(response.text)


whatsapp_message(payload=payload)

# api = os.environ.get("whatsaap_api")
# chat_id = os.environ.get("whatsapp_chatid")
# id_instance = os.environ.get("whatsapp_id_instance")
#
# endpoint = f"https://api.greenapi.com/waInstance{id_instance}/sendMessage/{api}"
#
# headers = {
#     'Content-Type': 'application/json'
# }
#

# payload = f"{{\r\n\t\"chatId\": \"{chat_id}\",\r\n\t\"message\": " \
#           f"\"{message}\"\r\n}}"
#
# response = requests.post(url=endpoint, headers=headers, data=payload)
#
# print(response.text)


