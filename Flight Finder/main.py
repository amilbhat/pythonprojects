from data_manager import DataManager
import datetime
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_CODE = "LON"

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_detination_code(row["city"])
    print(f"sheet_data: {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
future_six_month_date = datetime.datetime.now() + datetime.timedelta(days=180)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=future_six_month_date
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )



