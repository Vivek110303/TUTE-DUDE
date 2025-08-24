from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://www.google.com')
driver.maximize_window()

input_box = driver.find_element(By.NAME, 'q')
input_box.send_keys('selenium')

time.sleep(2)  # wait for suggestions to load, if necessary

button = driver.find_element(By.NAME, 'btnK')
button.click()

time.sleep(5)  # wait to see the results

driver.quit()
