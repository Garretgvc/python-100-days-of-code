from data_manager import DataManager
from flight_search import FlightSearch

flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# if sheet_data[0]["iataCode"] == "":
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get