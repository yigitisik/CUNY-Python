#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
import time
from dotenv import load_dotenv
import data_manager
import flight_search
from flight_data import find_cheapest_flight
import notification_manager
from datetime import datetime
from datetime import timedelta

AMADEUS_API_SECRET=os.getenv("AMAEDUS_API_SECRET")
AMADEUS_API_KEY=os.getenv("AMAEDUS_API_KEY")
SHEETY_BEARER_TOKEN=os.getenv("SHEETY_BEARER_TOKEN")
ORIGIN_IATA = "ORD"

sheet_manager = data_manager.DataManager()
sheet_data = sheet_manager.get_sheet_request()

fs = flight_search.FlightSearch()
nm = notification_manager.NotificationManager()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = fs.get_iata_code(city=row["city"])

    sheet_manager.row_data = sheet_data
    sheet_manager.put_sheet_request()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(180))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = fs.check_flights(
        ORIGIN_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )
        # SMS not working? Try whatsapp instead.
        nm.send_whatsapp(
            body=f"Low price alert! Only {cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )