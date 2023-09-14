from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(url)

# choose language

driver.find_element(By.CSS_SELECTOR, ".langSelectButton#langSelect-EN").click()




# try:
#     driver.find_element(By.CSS_SELECTOR, "#langSelect-EN").click()
# except NoSuchElementException:
#     print("using exception")
#     driver.find_element(By.XPATH, "//*[@id='langSelect-EN']").click()
# else:
#     clicking = True
#
#     while clicking:
#         start = time.time()
#         driver.find_element(By.ID, "bigCookie").click()
#         if time.time() == start + 5:
#             clicking = False
#             driver.find_elements(By.CSS_SELECTOR, "#products.product unlocked enabled")[-1].click()  # click on the most expensive but affordable product to buy it
#         clicking = True
#





