from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = 'laptop'
for i in range(1,20):
    driver.get(f"https://www.amazon.com/s?k={query}&ref=nav_bb_sb")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")  # Use find_elements (plural)
    print(f"{len(elems)} items found")
    for elem in elems:
        print(elem.text)
#print(elem.get_attribute("outerHTML"))
#print(elem.text)
time.sleep(5)
driver.close()
