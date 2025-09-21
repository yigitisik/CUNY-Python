import requests
from datetime import datetime as dt
import smtplib
import time

APP_PW = "dxeznufbnagffhrh"
ORIG_EMAIL = "mustafayigitisik749@gmail.com"
RECEIVER_EMAIL = "usa.mustafaisik@gmail.com"
MY_LAT = 44 #43.074223
MY_LNG = -140 #-89.45220
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

def iss_ideal_position():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()
    iss_pos_lat = float(data["iss_position"]["latitude"])
    iss_pos_lng = float(data["iss_position"]["longitude"])

    if (iss_pos_lat + 5 > MY_LAT > iss_pos_lat - 5) and (iss_pos_lng + 5 > MY_LNG > iss_pos_lng - 5):
        return True

def is_sun_down():
    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    data = sun_response.json()
    sunrise_hr = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hr = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.now().hour
    if  time_now < sunset_hr or time_now > sunrise_hr:
        return True

while True:
    time.sleep(60)
    if iss_ideal_position() and is_sun_down():
        try:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp_connection:
                smtp_connection.starttls()
                smtp_connection.login(user=ORIG_EMAIL, password=APP_PW)
                smtp_connection.sendmail(from_addr=ORIG_EMAIL, to_addrs=RECEIVER_EMAIL,
                                         msg=f"Subject: ISS Spotted\n\n Look up, ISS is in visible sky".encode("utf-8"))
        except Exception as e:
            print(f"{e}: Couldn't send an email to {RECEIVER_EMAIL} at this time. Try again later.")

