import os
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

WHATSAPP_CHAT_ID = os.environ.get("vancouver_trip")


ORIGIN_CITY_IATA = "YOW"

SEND_SMS = True

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        to_send = f"TravelBot: Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to " \
                  f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.\n{flight.link}"
        if SEND_SMS:
            notification_manager.send_sms(
                message=to_send
            )
        else:
            payload = f"{{\r\n\t\"chatId\": \"{WHATSAPP_CHAT_ID}\",\r\n\t\"message\": " \
                      f"\"{to_send}\"\r\n}}"
            notification_manager.send_whatsapp(payload=payload)

