from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

icon1= driver.find_element(By.CSS_SELECTOR,'#user-name')
icon2= driver.find_element(By.CSS_SELECTOR,'#password')
icon3= driver.find_element(By.CSS_SELECTOR,'#login-button')
if icon1 and icon2 and icon3 is not(None):
    print('Элементы найдены')
else:
    print('Элементы не найдены')