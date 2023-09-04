import os
import requests
from flight_search import FlightSearch
from data_manager import DataManager

# access sheety
sheety_bearer_auth = os.environ.get("sheety_bearer_auth")
sheety_headers = {
    "Authorization": f"Bearer {sheety_bearer_auth}"
}
SHEETY_ENDPOINT = "https://api.sheety.co/90a4d9f0bd0249ecf409b0665590a534/flightDeals/prices"


# access kiwi
kiwi_endpoint = "https://api.tequila.kiwi.com"
kiwi_location_headers = {
    "apikey": os.environ.get("kiwi_api"),
    "Content-Type": "application/json",
    "Content-Encoding": "gzip"
}

kiwi_search_headers = {
    "apikey": os.environ.get("kiwi_api"),
    "accept": "application/json"
}
kiwi_search_body = {
    "fly_from": "LON",
    "fly_to": "",
    "date_from": "",
    "date_to": "",
    "locale": "en",
    "curr": "CAD"

}

find_flights = FlightSearch(kiwi_endpoint, kiwi_location_headers, kiwi_search_headers)
data_manager = DataManager(sheety_headers=sheety_headers, flights=find_flights)


response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
data = response.json()["prices"]

for city in data:
    data_manager.add_iata_code(sheety_endpoint=SHEETY_ENDPOINT, city_row=city)

for code in data_manager.iata_codes:
    price = find_flights.search_cheap_flight(body=kiwi_search_body, destination=code)
    print(price)








