from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(url)

# choose language



# lang = driver.find_element(By.ID, "langSelect-EN")
# time.sleep(5)
# lang.click()

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "langSelect-EN"))).click()
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#bigCookie"))).click()


# try:
#     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "langSelect-EN"))).click()
# except NoSuchElementException:
#     print("Language already selected")
# else:
#     clicking = True
#
#     start = time.time()
#     while clicking:
#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#bigCookie"))).click()
#         if time.time() - 5 == start:
#             clicking = False
#             # driver.find_elements(By.CSS_SELECTOR, "#products.product unlocked enabled")[-1].click()  # click on the most expensive but affordable product to buy it
#         # clicking = True






