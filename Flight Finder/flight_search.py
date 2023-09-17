import requests
import datetime
from pprint import pprint
from flight_data import FlightData

TEQ_ENDPOINT = "https://api.tequila.kiwi.com"
TEQ_API_KEY = "TEQUILIA API KEY"


class FlightSearch:
    def get_detination_code(self, city_name):
        headers = {
            "apikey": TEQ_API_KEY
        }
        query = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(url=f"{TEQ_ENDPOINT}/locations/query",headers=headers, params=query)
        code = response.json()["locations"][0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        future_date = datetime.datetime.now() + datetime.timedelta(days=180)
        formatted_future_date = future_date.strftime("%d/%m/%Y")
        headers = {
            "apikey" : TEQ_API_KEY
        }
        params = {
            "fly_from" : origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(f"{TEQ_ENDPOINT}/v2/search" ,headers=headers, params=params)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"Sorry! No Flight was found for {destination_city_code}")
            return None
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data

