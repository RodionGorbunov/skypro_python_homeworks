# открываем страницу в браузере Firefox
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://uitestingplayground.com/dynamicid/")

# три раза кликнуть по синей кнопке
for x in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
    sleep(1)

sleep(5)
driver.quit()
