import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

url = "https://ca.linkedin.com/jobs"
EMAIL = os.environ.get("email")
PW = os.environ.get("password")
SEARCH_TERM = "Python developer"

driver.get(url=url)

# login
driver.find_element(By.ID, "session_key").send_keys(EMAIL)
driver.find_element(By.ID, "session_password").send_keys(PW, Keys.ENTER)

# search jobs
driver.find_element(By.ID, "jobs-search-box-keyword-id-ember24").send_keys(SEARCH_TERM, Keys.ENTER)

# get jobs list
time.sleep(5)
jobs = driver.find_elements(By.CSS_SELECTOR, "ul li div.full-width a")
# jobs = WebDriverWait(driver, 30).until(lambda d: d.find_elements(By.CSS_SELECTOR, "ul li div.full-width a"))

for job in jobs[:2]:
    print("Saving jobs")
    job.click()
    time.sleep(3)
    # driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.jobs-save-button"))).click()  # save job
    print("saved job")

    print("following company")
    # driver.find_element(By.ID, "ember85").click()
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll page to the bottom
    time.sleep(3)
    follow = driver.find_element(By.CSS_SELECTOR, "button.follow")
    driver.execute_script("arguments[0].click();", follow)
    print("followed company")

driver.quit()
