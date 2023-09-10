import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
title_tag = soup.select(selector=".titleline a")
scores_tag = soup.select(selector=".score")

titles = [tag.getText() for tag in title_tag]
links = [tag.get("href") for tag in title_tag]
scores = [int(tag.getText().split(" ")[0]) for tag in scores_tag]

index = scores.index(max(scores))

print(titles[index])
print(links[index])

# print(len(titles) == len(scores))
#
# print(titles)
# print(links)
# print(scores)








# with open("./website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title.string)
#
# links = soup.find_all(name="a")
#
# for tag in links:
#     # print(tag["href"])
#     # print(tag.get("href"))
#     # print(tag.getText())
#     pass
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
# company_url = soup.select_one(selector="p a")
# # print(company_url.get("href"))
#
# # links = soup.select(selector="ul a")
# # print(links)
#
# # max_length = soup.select_one(selector="form input")
# max_length = soup.find("input")
# print(max_length.get("maxlength"))
