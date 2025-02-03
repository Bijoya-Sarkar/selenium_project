from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = 'laptop'
file = 0
for i in range(1,20):
    driver.get(f"https://www.amazon.com/s?k={query}&ref=nav_bb_sb")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")  # Use find_elements (plural)
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute('outerHTML')
        with open(f"data/{query}_{file}.html","w",encoding="utf-8") as f:
            f.write(d)
            file += 1
#print(elem.get_attribute("outerHTML"))
#print(elem.text)
    time.sleep(5)
driver.close()
