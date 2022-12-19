import requests
import os
from datetime import datetime

USERNAME = os.environ["USERNAME"]
TOKEN = os.environ["TOKEN"]
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}
graph_config = {
    "id": "graph1",
    "name": "Daily Coding graph",
    "unit": "hr",
    "type": "float",
    "color": "sora",
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_data_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

date = datetime.now()
date_string = date.strftime("%Y%m%d")

hours_of_coding = 5.3

graph_data = {
    "date": f"{date_string}",
    "quantity": f"{hours_of_coding}",
}

# response = requests.post(url=graph_data_endpoint, json=graph_data, headers=headers)
# print(response.text)

date_to_edit = datetime(year=2022, month=12, day=14)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_edit.strftime('%y%m%d')}"

data_to_edit = {
    "quantity": "8.0"
}

# response = requests.put(url=update_endpoint, json=data_to_edit, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_edit.strftime('%y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
