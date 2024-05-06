# открываем страницу в браузере Chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/login")

driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys("tomsmith")

driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, 'i.fa').click()

sleep(5)
driver.quit()

# открываем страницу в браузере Firefox

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys("tomsmith")

driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, 'i.fa').click()

sleep(5)
driver.quit()
