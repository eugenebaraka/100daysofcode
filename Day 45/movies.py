import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")[::-1]

with open("movies.txt", "w") as file:
    for movie in all_movies:
        file.write(f"{movie.getText()}\n")

