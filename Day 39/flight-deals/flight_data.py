import datetime as dt
from pyshorteners import Shortener
from flight_search import FlightSearch

str_date_fmt = "%Y-%m-%dT%H:%M:%S.%fZ"
dt_format = "%Y-%m-%d"


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, flights: FlightSearch):
        self.flights = flights

    def get_cheapest_flight(self, body: dict, destination: str):
        flights = self.flights.search_cheap_flight(body=body, destination=destination)

        cheapest_flight = flights[0]
        new_price = cheapest_flight["price"]

        from_date = cheapest_flight["route"][0]["local_departure"]
        from_date = dt.datetime.strptime(from_date, str_date_fmt).strftime(dt_format)
        to_date = cheapest_flight["route"][-1]["local_arrival"]
        to_date = dt.datetime.strptime(to_date, str_date_fmt).strftime(dt_format)

        nights = cheapest_flight["nightsInDest"]
        link = Shortener().tinyurl.short(cheapest_flight["deep_link"])

        cheap_flight = {"from_date": from_date,
                        "to_date": to_date,
                        "new_price": new_price,
                        "nights": nights,
                        "link": link}
        # print(cheapest_flight["deep_link"])
        # print(link)

        return cheap_flight
