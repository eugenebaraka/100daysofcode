import os

import requests

APP_ID = os.environ.get("app_id")
API_KEY = os.environ.get("nutritionix_api_key")


ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

today_exercise = input("What did you do today and for how long? ")

exercise_params = {
    "query": today_exercise,
}

response = requests.post(url=ENDPOINT, json=exercise_params, headers=headers)
print(response.json())





