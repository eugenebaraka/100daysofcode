from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

url = "https://www.amazon.ca/gp/product/B0B2X Y/ref=ox_sc_act_title_1?smid=A3DWYIK6Y9EEQB&th=1"

driver.get(url)

price = driver.find_element(By.CLASS_NAME, "aok-offscreen").text
print(price)


# driver.close() # closes the current tab
driver.quit()  # closes the entire browser

