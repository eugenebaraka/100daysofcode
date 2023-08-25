import requests

LAT = 45.501690
LONG = -73.567253
url = "https://api.sunrise-sunset.org/json"

params = {
    "lat": LAT,
    "long": LONG,
    "formatted": 0
}

response = requests.get(url=url, params=params)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunset)
