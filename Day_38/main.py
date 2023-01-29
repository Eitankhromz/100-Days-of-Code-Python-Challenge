import requests
import os
from datetime import datetime

APP_ID = os.environ["xxxx"]
API_KEY = os.environ["xxxx"]
NUTRITIONX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/"xxxx"/workoutTracking/workouts"
AUTH_TOKEN = os.environ["xxxx"]

user_input = input("Tell me which exercises you did?: ")


headers = {
    "x-app-id": os.environ.get(APP_ID),
    "x-app-key": os.environ.get(API_KEY),
}


body_params = {
    "query": user_input,
    "gender": "male",
    "height_cm": 175,
    "weight_kg": 68,

}

response = requests.post(url=NUTRITIONX_ENDPOINT, json=body_params, headers=headers)
response.raise_for_status()
results = response.json()



today = datetime.now().strftime("%x")
time_now = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": os.environ.get(AUTH_TOKEN)
}


for exercise in results["exercises"]:
    sheety_data = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        },
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_data, headers=bearer_headers)
    print(sheety_response.text)
