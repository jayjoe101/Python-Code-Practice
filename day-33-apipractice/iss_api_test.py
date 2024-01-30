import requests
from datetime import datetime
from time import sleep

# ISS API

response = requests.get(url="http://api.open-notify.org/iss-now.json")

"""
HTTP CODES:
1XX: Hold On
2XX: Here you go
3XX: Go Away
4XX: You Screwed Up
5XX: I Screwed Up
"""

if response.status_code != 200:
    raise Exception(response.raise_for_status()) # This will raise an exception if the status code is not 200

data = response.json()["iss_position"] # This is the same as data.get("iss_position")

lng = float(data["longitude"]) # This is the same as data.get("longitude")
lat = float(data["latitude"]) # This is the same as data.get("latitude")

iss_position = (lng, lat) # This is the same as iss_position = (data.get("longitude"), data.get("latitude"))
# print(iss_position)

# Sunrise and Sunset API

params = {
    "lat": lat,
    "lng": lng,
    "formatted": 0 # This is to get the time in 24 hour format, default is a 12 hour format
}

sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)

if sunset_response.status_code != 200:
    raise Exception(sunset_response.raise_for_status())

sunset_data = sunset_response.json()
# print(sunset_data)

"""
in https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
before the ? is the endpoint
after the ? are the parameters
the parameters are separated by & (just add & to add more parameters)
lat=36.7201600 is a parameter
lng=-4.4203400 is a parameter
"""

sunrise_time = int(sunset_data["results"]["sunrise"].split("T")[1].split(":")[0]) # This is to get the hour from the time
sunset_time = int(sunset_data["results"]["sunset"].split("T")[1].split(":")[0]) # This is to get the hour from the time

timenow = datetime.now().hour # This is to get the hour from the time
# print(sunset_time, sunrise_time, timenow)

my_lat = 33.462201
my_lng = -81.992020

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()["iss_position"] # This is the same as data.get("iss_position")

    lng = float(data["longitude"]) # This is the same as data.get("longitude")
    lat = float(data["latitude"]) # This is the same as data.get("latitude")
    params = {
    "lat": lat,
    "lng": lng,
    "formatted": 0 # This is to get the time in 24 hour format, default is a 12 hour format
    }
    sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    
    sunset_data = sunset_response.json()
    sunrise_time = int(sunset_data["results"]["sunrise"].split("T")[1].split(":")[0]) # This is to get the hour from the time
    sunset_time = int(sunset_data["results"]["sunset"].split("T")[1].split(":")[0]) # This is to get the hour from the time

    if my_lat-5 <= lat <= my_lat+5 and my_lng-5 <= lng <= my_lng+5 and sunset_time <= timenow <= sunrise_time: # This is to check if the ISS is within 5 degrees of my location and if it is night time
            print("Look up!")

while True:
    if datetime.now().second % 60 == 0: # This is to check if it is the start of a new minute
        if is_iss_overhead():
            print("Look up!")
        else:
            print("The ISS is not above you right now.")
    sleep(1) # This is to sleep for 1 second before checking again