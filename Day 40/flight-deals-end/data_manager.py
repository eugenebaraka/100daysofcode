import os
from pprint import pprint
import requests

ACC_NUM = "90a4d9f0bd0249ecf409b0665590a534"

SHEET = "prices"
SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{ACC_NUM}/flightDeals/{SHEET}"
headers = {
    "Authorization": f"Bearer {os.environ.get('sheety_bearer_auth')}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)
