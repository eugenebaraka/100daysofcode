import datetime
import re

import requests
import datetime as dt


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self, kiwi_endpoint: str, location_headers: dict, search_headers: dict):
        self.kiwi_endpoint = kiwi_endpoint
        self.kiwi_location_headers = location_headers
        self.kiwi_search_headers = search_headers

    def search_iata(self, params: dict):
        kiwi_location_endpoint = f"{self.kiwi_endpoint}/locations/query"
        response = requests.get(url=kiwi_location_endpoint, params=params, headers=self.kiwi_location_headers)
        code = response.json()["locations"][0]["code"]
        return code

    def search_cheap_flight(self, body: dict, destination: str):
        # start search from tomorrow
        tomorrow = dt.datetime.today() + datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime("%d/%m/%Y")
        after_six_months = dt.datetime.today() + datetime.timedelta(days=6*30)
        after_six_months = after_six_months.strftime("%d/%m/%Y")

        get_iata = re.search("([a-zA-Z]*-)([A-Z]*)", body["fly_from"])
        body["fly_from"] = get_iata[2]
        body["fly_to"] = destination
        body["date_from"] = tomorrow
        body["date_to"] = after_six_months

        kiwi_search_endpoint = f"{self.kiwi_endpoint}/v2/search"

        response = requests.get(url=kiwi_search_endpoint, params=body, headers=self.kiwi_search_headers)

        flights = response.json()["data"]

        # return fly_from name to original form
        body["fly_from"] = get_iata[0]

        return flights

