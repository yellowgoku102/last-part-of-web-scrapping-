from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

elem = driver.find_element(By.CLASS_NAME, "_75nlfW")
print(elem.get_attribute("outerHTML"))


time.sleep(4)
driver.close()
