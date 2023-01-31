import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/16f095c94544a54df5d4fa3d0bfc15e2/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        pprint(data)
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_data(self):

        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

