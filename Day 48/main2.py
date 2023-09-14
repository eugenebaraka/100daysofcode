import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

url = "https://www.python.org/"

driver.get(url)

times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# for event in events_html:
#     print(event.text)

events = {}

for n in range(len(times)):
    events[n] = {
        "time": times[n].text,
        "name": names[n].text
    }

print(events)
driver.quit()

