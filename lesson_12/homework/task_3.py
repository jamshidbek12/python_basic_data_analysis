from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

import time

chrome_options = Options()
# chrome_options.add_argument("--window-position=-2000,-100")  # Position window on the second screen
chrome_options.add_argument("--window-position=1020,0")

driver = webdriver.Chrome(chrome_options)

driver.get('https://www.demoblaze.com/')
xpath = """//*[@id="itemc"]"""

time.sleep(2)
element = driver.find_element(By.XPATH, "//a[@onclick=\"byCat(\'notebook\')\"]")
element.click()
time.sleep(3)

data = []
contents = driver.find_elements(By.CLASS_NAME, "card-block") 
for content in contents:
    name = content.find_element(By.TAG_NAME, 'a')
    price = content.find_element(By.TAG_NAME, 'h5')
    description = content.find_element(By.TAG_NAME, 'p')
    print(f"{name.text}\n {price.text}\n {description.text}")
    print("-"*30)
    data.append({'name': name.text, 'price': price.text, 'description': description.text})
time.sleep(5)
driver.quit()

with open('data.json', 'wt') as file:
    writer = json.dump(data, file, indent=2)
    print("Successfully saved")
