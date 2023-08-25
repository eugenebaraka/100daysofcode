import keyring
import requests
from datetime import datetime
import smtplib

email = "eugenebaraka@gmail.com"
password = keyring.get_password("10daysofcode", email)

MY_LAT = 45.501690
MY_LONG = -73.567253

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

iss_is_close = (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) & \
               (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)
is_dark = (time_now <= sunrise or time_now >= sunset)

if iss_is_close & is_dark:  # iss is within +/-5 degrees and it's dark
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email,
                            msg="Subject: The ISS is above you\n\nGo outside now to "
                                "check it out")
