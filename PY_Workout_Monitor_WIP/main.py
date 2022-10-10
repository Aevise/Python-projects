import requests
from datetime import datetime
import pprint
import os

#---------personal data ----------------
GENDER = "male"
WEIGHT = 90
HEIGHT = 183
AGE = 27


os.environ['NUTRI_API_ID_ENV'] = "2faf6dba"
print(os.environ['NUTRI_API_ID_ENV'])
#---------nutri data -------------------
NUTRI_WEBSITE = "https://trackapi.nutritionix.com"
NUTRI_ENDPOINTS = {
    "Food Lookup Endpoints": "/v2/natural/nutrients",
    "Food Database": "/v2/search/instant",
    "Exercise Endpoints": "/v2/natural/exercise",
    "Location Endpoint": "/v2/locations"
}
NUTRI_API_ID = "2faf6dba"
NUTRI_API_KEY = "ba6b43f8ec8697ab2414c064f7cf82ec"
NUTRI_HEADER = {
    "x-app-id": NUTRI_API_ID,
    "x-app-key": NUTRI_API_KEY
}

#----------sheety data -----------------------
SHEETY_WEBSITE = "https://api.sheety.co/d035a3965e1dd128967d629de683efab/workoutApi/arkusz1"
TOKEN ={
    "Authorization": "Bearer kjfvchn87q36457289rfsndfg67235tsdgf"
}

my_exercise = input("Today I have worked out as follows: ")
nutri_params = {
    "query": my_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

r = requests.post(url = (NUTRI_WEBSITE+NUTRI_ENDPOINTS["Exercise Endpoints"]), json = nutri_params, headers = NUTRI_HEADER)
workout_data = r.json()
pprint.pprint(workout_data)

# ------------- add data ------------------
today = datetime.now().strftime("%Y-%m-%d")
now_hour = datetime.now().strftime("%X")
for exercise in workout_data["exercises"]:
    processed_workout_data = {
        "arkusz1": {
            "date": today,
            "time": now_hour,
            "exercise": exercise['name'].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    r2 = requests.post(url=SHEETY_WEBSITE, json=processed_workout_data, headers=TOKEN)
# ----------------------------------------

