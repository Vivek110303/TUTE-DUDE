from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.amazon.in')

driver.maximize_window()
time.sleep(5)

electronics_link = driver.find_element(By.LINK_TEXT, 'Electronics')
electronics_link.click()

time.sleep(5)

try:
    audio_link = driver.find_element(By.LINK_TEXT, 'Audio')
except:
    audio_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Audio')
audio_link.click()

time.sleep(5)

driver.quit()
