from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.amazon.in')
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys('iphones')
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()

items = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
print(str(len(items)) + ' products found')

for i in items:
    print(i.text)

driver.quit()
