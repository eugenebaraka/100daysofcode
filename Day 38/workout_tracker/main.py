import os
import datetime as dt
import requests

APP_ID = os.environ.get("app_id")
API_KEY = os.environ.get("nutritionix_api_key")
SHEETY_ENDPOINT = os.environ.get("sheety_endpoint")
BEARER_AUTH = os.environ.get("sheety_bearer_auth")


ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

today_exercise = input("What did you do today and for how long? ")

exercise_params = {
    "query": today_exercise,
}

response = requests.post(url=ENDPOINT, json=exercise_params, headers=headers)
data = response.json()["exercises"]
# print(response.json())

# populate values in the sheet
sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BEARER_AUTH}"
}

# get exercise row values
now = dt.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.time().strftime("%H:%M:%S")

for type_exercise in data:
    calories = type_exercise["nf_calories"]
    duration = type_exercise["duration_min"]
    exercise = type_exercise["name"]

    body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise.capitalize(),
            "duration": duration,
            "calories": calories
        }
    }

    # add exercise row
    add_row_response = requests.post(url=SHEETY_ENDPOINT, json=body, headers=sheety_headers)
    print(add_row_response.text, end=" ")
