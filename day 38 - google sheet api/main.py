import requests
from datetime import datetime as dt
import os

DATE = dt.now().strftime("%x")
TIME = dt.now().strftime("%H:%M")

NUTRITIONIX_APP_ID = "95a99003"
NUTRITIONIX_APP_KEY = "68906e88333b3a2e166a5a52fc150140"

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/4d9e78777afe3943e092b85cb54d8706/myiWorkouts/workouts"

HEADERS = {
    "x-app-id": os.environ.get("NUTRITIONIX_APP_ID"),
    "x-app-key": os.environ["NUTRITIONIX_APP_KEY"],
    "x-remote-user-id": "0",
}

query = {
    "query": input("Tell me which exercises you did: "),
}

nutritionix_post_resp = requests.post(
    url=NUTRITIONIX_ENDPOINT,
    data=query,
    headers=HEADERS
)
nutritionix_post_resp.raise_for_status()
print(nutritionix_post_resp.text)

workout_json = nutritionix_post_resp.json()

sheety_header = {
    "Authorization": f"Bearer {os.environ['BEARER_TOKEN']}",
}

for exercise in workout_json["exercises"]:
    sheety_params = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheety_post_resp = requests.post(
        url=SHEETY_ENDPOINT,
        json=sheety_params,
        headers=sheety_header
    )
    print(sheety_post_resp.text)
