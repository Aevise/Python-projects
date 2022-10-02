from datetime import datetime
from multiprocessing.sharedctypes import Value
import requests

def add_data()->None:
    """Adds a value to the pixel in Pixela API
    """
    pixels_endpoint = f"{graph_endpoint}/{GRAPH_PARAMS['id']}"
    now = datetime.now()
    current_day = now.day
    if current_day < 10:     
        current_day = "0" + str(current_day)
    date_to_fill = str(now.year)+str(now.month)+current_day
    print(date_to_fill)
    incorrect = True

    while incorrect:
        try:
            kilometers = str(float(input("I have ran: ")))
        except ValueError:
            pass
        else:
            incorrect = False

    pixels_params = {
        "date": date_to_fill,
        "quantity": kilometers
    }

    add_data = requests.post(url = pixels_endpoint, json = pixels_params, headers = header)
    print(add_data.text)

def update_data()->None:
    incorrect = True
    while incorrect:
        try:
            new_value = str(float(input("I have ran: ")))
            day_to_update = str(int(input("Enter a day to update in format: yyymmdd ex. 20221002")))
        except ValueError:
            print("Please enter the correct value")
        else:
            incorrect = False
    
    pixels_endpoint = f"{graph_endpoint}/{GRAPH_PARAMS['id']}/{day_to_update}"
    pixel_params = {
        "quantity": new_value
    }
    update_data = requests.put(url = pixels_endpoint, params = pixel_params, headers = header)
    print(update_data.text)


USER = "user"
TOKEN = "token"
PIXELA_WEBSITE = "https://pixe.la/v1/users"
PIXELA_PARAMS = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_endpoint = f"{PIXELA_WEBSITE}/{USER}/graphs"
GRAPH_PARAMS = {
    "id": "mygraph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float", 
    "color": "sora",
}
header = {
    "X-USER-TOKEN": TOKEN
}


create_account = requests.post(url = PIXELA_WEBSITE, json = PIXELA_PARAMS)
response = requests.post(url = graph_endpoint, json = GRAPH_PARAMS, headers = header)
add_data()
update_data()


