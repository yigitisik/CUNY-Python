import requests
from datetime import datetime as dt

parameters = {
    "lat": 43.074223,
    "lng": -89.45220,
    "formatted": 0,
    "tzid": "America/Chicago",
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
url = response.url
print(url)

data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1]
sunrise_hr = sunrise.split(":")[0]
sunrise_min = sunrise.split(":")[1]

sunset = data["results"]["sunset"].split("T")[1]
sunset_hr = sunset.split(":")[0]
sunset_min = sunset.split(":")[1]

time_now = str(dt.now()).split(" ")[1]
now_hr = time_now.split(":")[0]
now_mint = time_now.split(":")[1]


