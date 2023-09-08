from flight_search import *

LOCATION_PARAMS = {
    "term": None,
    "locale": "en-US",
    "location_types": "city",
    "active_only": True,
    "limit": 1
}

NEW_ROW = {
    "price": {
        "city": None,
        "iataCode": None,
        "lowestPrice": None
    }
}


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self, sheety_endpoint: str, sheety_headers: dict, flights: FlightSearch):
        self.sheety_endpoint = sheety_endpoint
        self.sheety_headers = sheety_headers
        self.flights = flights

    def add_iata_code(self, city_row: dict):
        city = city_row["city"]
        LOCATION_PARAMS["term"] = city
        iata_code = self.flights.search_iata(params=LOCATION_PARAMS)

        NEW_ROW["price"]["city"] = city
        NEW_ROW["price"]["iataCode"] = iata_code
        price = city_row["lowestPrice"]
        NEW_ROW["price"]["lowestPrice"] = price

        row_num = city_row["id"]
        row_url = f"{self.sheety_endpoint}/{row_num}"

        requests.put(url=row_url, json=NEW_ROW, headers=self.sheety_headers)

    def get_current_data(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        print(response.text)
        data = response.json()["prices"]

        return data
