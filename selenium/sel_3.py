from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://www.google.com')
driver.maximize_window()

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('selenium')
time.sleep(5)

search_button = driver.find_element(By.NAME, 'btnK')
search_button.click()

time.sleep(5)
driver.back()

time.sleep(5)
driver.forward()

time.sleep(5)
driver.quit()
