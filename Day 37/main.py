import requests
import datetime as dt


USERNAME = "barakatest"
TOKEN = "1hk3h4k5m0j0pe9jj1n5lwhhlbncdklsurgdirn0d"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# I. CREATE ACCOUNT
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=params)
# print(response.text)

# II. CREATE A GRAPH
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "color": "ajisai",  # purple
    "unit": "Km",
    "type": "float"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# III. ADD A PIXEL
today = dt.datetime.today().strftime("%Y%m%d")


PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_params = {
    "date": today,
    "quantity": "15"
}
# response_pixel = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)
# print(response_pixel.text)

# IV. USING PUT
UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
new_pixel = {
    "quantity": "9"
}
response_put = requests.put(url=UPDATE_ENDPOINT, json=new_pixel, headers=headers)
print(response_put.text)


