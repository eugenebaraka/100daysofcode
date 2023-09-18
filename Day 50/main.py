import time
from selenium.webdriver.common.by import By
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

url = "https://tinder.com/"

driver.get(url)

# decline cookies
time.sleep(5)
login = driver.find_element(By.LINK_TEXT, "Log in")
driver.execute_script("arguments[0].click();", login)

driver.find_element(By.ID, "button-label").click()

time.sleep(5)

# driver.quit()
