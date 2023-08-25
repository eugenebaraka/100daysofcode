import requests

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
data = response.json()


long = data["iss_position"]['latitude']
lat = data["iss_position"]['longitude']
print(long)
print(lat)
