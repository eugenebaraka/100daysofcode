import requests
from bs4 import BeautifulSoup
import lxml
import pprint

pp = pprint.PrettyPrinter(indent=4)

url = "https://www.amazon.ca/gp/product/B0B2XLX86Y/ref=ox_sc_act_title_1?smid=A3DWYIK6Y9EEQB&th=1"
headers = {
    "ACCEPT-LANGUAGE": "fr-FR,fr;q=0.6",
    "USER-AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

response = requests.get(url=url, headers=headers).content

soup = BeautifulSoup(response, "lxml")

price = soup.find(name="span", class_="a-offscreen").getText()
price = price.split("$")[1]  # remove dollar sign
print(price)
