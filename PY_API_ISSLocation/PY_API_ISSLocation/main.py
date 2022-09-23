import requests, json, datetime



ISS_WEBSITE = "http://api.open-notify.org/iss-now.json"
SUNSET_WEBSITE = "https://api.sunrise-sunset.org/json"
MY_LOCATION = {
    "lat": 51.10956787281795, 
    "lon": 17.0335723207322
}

def get_iss_position()->None:
    """gets the current position of ISS.
    """
    iss_response = requests.get(url = ISS_WEBSITE)
    iss_response.raise_for_status()
    data = iss_response.json()
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    return (latitude, longitude)

def iss_nearby(iss_location:tuple)->bool:
    global MY_LOCATION
    if (MY_LOCATION["lat"] - float(iss_location[0]) in range(-5,6)) and (MY_LOCATION["lon"] - float(iss_location[1]) in range(-5,6)):
        return True
    else:
        return False

def iss_visible(iss_position:tuple, sunrise, sunset):
    current_time = datetime.datetime.now()
    current_hour = current_time.hour
    if iss_nearby(iss_position):
        if current_hour > sunrise and current_hour >= sunset:
            print("You can see ISS from your location.")
        else:
            print("It's too bright to see the ISS. Please be patient and try again next time when it's dark.")
    else:
        print("You will not be able to see ISS from your location.")


iss_position = get_iss_position()


# --------------------------- information for the ISS location ------------------
#parameters = {
#    "lat": iss_position[0],
#    "lon": iss_position[1],
#    "formatted": 0
#}
#
#sun_response = requests.get(url = SUNSET_WEBSITE, params = parameters)
#sun_response.raise_for_status()
#data = sun_response.json()
#
#sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
#sunrise = data["results"]["sunrise"]
#list_data = sunrise.split("T")
#sunrise = int(list_data[1].split(":")[0])

parameters = {
    "lat": MY_LOCATION["lat"],
    "lon": MY_LOCATION["lon"],
    "formatted": 0
}

sun_response = requests.get(url = SUNSET_WEBSITE, params = parameters)
sun_response.raise_for_status()
data = sun_response.json()
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
sunrise = data["results"]["sunrise"]
list_data = sunrise.split("T")
sunrise = int(list_data[1].split(":")[0])
print("ISS position", iss_position, f"My position: {MY_LOCATION['lat'], MY_LOCATION['lon']}")
print("My location -> sunrise: ", sunrise, "sunset: ", sunset)

iss_visible(iss_position, sunrise, sunset)


