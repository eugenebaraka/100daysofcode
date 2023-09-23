# STEPS
# 1. GET THE HTML OF THE DESIRED PROPERTIES (BASED ON FEATURES) USING BS4
# 2. FILL OUT THE GOOGLE FORM USING SELENIUM
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url_base = "https://www.kijiji.ca"
properties_url = f"{url_base}/b-apartments-condos/quebec/montreal-rent-apartment/1+bathroom-1+bedroom/k0c37l9001a120a27949001"

response = requests.get(url=properties_url).content
soup = BeautifulSoup(response, "html.parser")

all_listings = soup.select(selector="ul.sc-a3fd170-0.cJBcel li div.sc-2e07e5ea-4")

# access google form
google_form = "https://forms.gle/oSJg7jJY573M2KpC9"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless")

for listing in all_listings:
    title_element = listing.select_one(selector="h3.sc-c54bbc09-0 a")
    title = title_element.text

    link = f"{url_base}{title_element['href']}"

    driver = webdriver.Chrome(options=options)
    driver.get(url=google_form)
    time.sleep(2)
    link_box = driver.find_element(By.XPATH,
                                   "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_box.send_keys(link)

    price = listing.select_one(selector="div.sc-57d74591-0 p").text
    price_box = driver.find_element(By.XPATH,
                                    "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_box.send_keys(price)

    location = listing.select_one(selector="div.sc-458a6da3-0 p").text
    address_box = driver.find_element(By.XPATH,
                                      "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address_box.send_keys(location)

    submit_button = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

    submit_button.click()

    driver.quit()
