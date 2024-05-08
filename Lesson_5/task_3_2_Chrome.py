# открываем страницу в браузере Chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid/")

# три раза кликнуть на синюю кнопку
for x in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
    sleep(1)

sleep(5)
driver.quit()
