import requests

DATA_LOCATION = "https://opentdb.com/api.php?"
QUESTION_PARAMS= {
    "amount": 10,
    "type": "boolean"
}

def get_data():
    data = requests.get(DATA_LOCATION, params = QUESTION_PARAMS)
    data.raise_for_status()
    data = data.json()
    data.pop("response_code")
    return data["results"]

database = get_data()
