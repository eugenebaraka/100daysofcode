import requests


def get_data(url: str, params: dict):
    response = requests.get(url, params=params)
    response.raise_for_status()
    question_data = response.json()["results"]

    return question_data
