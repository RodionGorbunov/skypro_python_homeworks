# открываем страницу в браузере Chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

# в модальном окне нажать на кнопку Сlose
# 'div.modal-footer p'
# '//*[@id="modal"]/div[2]/div[3]/p'
driver.find_element(By.CSS_SELECTOR, "div.modal-footer p").click()

sleep(5)
driver.quit()

# открываем страницу в браузере Firefox

from selenium import webdriver

driver = webdriver.Firefox()

# открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

# в модальном окне нажать на кнопку Сlose
# 'div.modal-footer p'
# '//*[@id="modal"]/div[2]/div[3]/p'
driver.find_element(By.CSS_SELECTOR, "div.modal-footer p").click()

sleep(5)
driver.quit()
