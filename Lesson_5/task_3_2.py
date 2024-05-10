# открываем страницу в браузере Chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid/")

# три раза кликнуть на синюю кнопку
for x in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
    sleep(1)

sleep(5)
driver.quit()

# открываем страницу в браузере Firefox

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://uitestingplayground.com/dynamicid/")

# три раза кликнуть по синей кнопке
for x in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
    sleep(1)

sleep(5)
driver.quit()
