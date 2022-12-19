import requests
from datetime import datetime
import os

API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
BEARER = os.environ.get("BEARER")

GENDER = "male"
WEIGHT = "77.0"  # kg
HEIGHT = "192.0"  # cm
AGE = "29"

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

input_text = input("What exercise did you do today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
    "query": input_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(nutrition_endpoint, json=params, headers=headers)
print(response.json())
result = response.json()

bearer_header = {
    "Authorization": BEARER
}

for exercise in result["exercises"]:
    inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(sheety_endpoint, json=inputs, headers=bearer_header)

    print(sheety_response.text)
