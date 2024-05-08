# открываем страницу в браузере Chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# открыть страницу
driver.get("http://the-internet.herokuapp.com/inputs")
Element = 'input'
click = driver.find_element(By.CSS_SELECTOR, Element)
click.send_keys("1000")
sleep(3)
click.clear()
sleep(2)
# ввести в это же поле текст 999
click.send_keys("999")

sleep(2)
driver.quit()
