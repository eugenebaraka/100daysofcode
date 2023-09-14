from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

# url = "https://en.wikipedia.org/wiki/Main_Page"

# driver.get(url)

# driver.find_element(By.CSS_SELECTOR, "#articlecount a").click()

# print(n_articles)

# driver.quit()

# create_acct = driver.find_element(By.LINK_TEXT, "View history")
# create_acct.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python", Keys.ENTER)
# search.send_keys(Keys.ENTER)


url = "http://secure-retreat-92358.herokuapp.com"

driver.get(url)

fName = driver.find_element(By.NAME, "fName")
fName.send_keys("eugene")
lName = driver.find_element(By.NAME, "lName")
lName.send_keys("LastNameBaby")
email = driver.find_element(By.NAME, "email")
email.send_keys("MyEmailBaby@email.com")

driver.find_element(By.CSS_SELECTOR, "form button").click()

