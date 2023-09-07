import requests
import os

bearer_auth = os.environ.get("sheety_bearer_auth")

project = "flightDeals"
sheet = "users"
base_endpoint = "https://api.sheety.co/90a4d9f0bd0249ecf409b0665590a534"


def post_new_row(fname: str, lname: str, email: str):
    endpoint = f"{base_endpoint}/{project}/{sheet}"

    headers = {
        "Authorization": f"Bearer {bearer_auth}"
    }

    user_details = {
        "user": {
            "firstName": fname,
            "lastName": lname,
            "email": email
        }
    }

    response = requests.post(url=endpoint, json=user_details, headers=headers)
    print(response.text)

    if response.status_code != 200:
        print("Something went wrong. Try again later")
    else:
        print("You are in the club!")


print("Welcome to myFlightClub\nWe find the best flight deals and email you.")

fname = input("What is your first name? ")
lname = input("What is your last name? ")

email = input("What is your email? ")
email_again = input("Type your email again. ")

while email != email_again:
    print("The emails do not match. Let's start over")
    email = input("What's your email address? ")
    email_again = input("Type your email again. ")

post_new_row(fname, lname, email)







