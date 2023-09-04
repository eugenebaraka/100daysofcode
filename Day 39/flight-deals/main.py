import os
import requests

from flight_search import FlightSearch
from data_manager import DataManager
import datetime as dt
from flight_data import FlightData
from notification_manager import NotificationManager

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
    "apikey": os.environ.get("kiwi_api")
}
kiwi_search_body = {
    "fly_from": "Ottawa-YOW",
    "fly_to": "",
    "date_from": "01/09/2023",
    "date_to": "01/10/2023",
    "return_from": "01/09/2023",
    "return_to": "01/12/2023",
    "locale": "en",
    "curr": "CAD",
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 14,
    "limit": 1

}

find_flights = FlightSearch(kiwi_endpoint=kiwi_endpoint, location_headers=kiwi_location_headers,
                            search_headers=kiwi_search_headers)
data_manager = DataManager(sheety_headers=sheety_headers, flights=find_flights, sheety_endpoint=SHEETY_ENDPOINT)
cheap_flight = FlightData(flights=find_flights)
notifications = NotificationManager(kiwi_search_body=kiwi_search_body)
data = data_manager.get_current_data()

for flight_row in data:
    city_code, price = data_manager.add_iata_code(city_row=flight_row)
    cheapest_flight = cheap_flight.get_cheapest_flight(body=kiwi_search_body, destination=city_code)

    if float(cheapest_flight["new_price"]) < float(price):
        city = flight_row["city"]
        iata = flight_row["iataCode"]
        notifications.send_message(to_city=city, to_iata=iata, cheapest_flight=cheapest_flight, whatsapp=True)
