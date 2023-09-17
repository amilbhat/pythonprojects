import requests
from pprint import pprint

SHEETY_URL = "SHEETY URL HERE"

class DataManager:
    def __init__(self) -> None:
        self.destination_data = {}

    def get_destination(self):
        response = requests.get(url=SHEETY_URL)
        result = response.json()
        self.destination_data = result["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        for data in self.destination_data:
            updated_data = {
                "price" : {
                    'iataCode': data["iataCode"]
                }
            }
            response = requests.put(
                url= f"{SHEETY_URL}/{data['id']}",
                json=updated_data
            )

            print(response.text)