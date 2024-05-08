# открываем страницу в браузере Firefox
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr/")
Add_dElement = 'button.btn-primary'
click = driver.find_element(By.CSS_SELECTOR, Add_dElement)

# три раза кликнуть на синюю кнопку
for x in range(3):
    click.click()
    a = driver.switch_to.alert.accept()
    sleep(1)

sleep(5)
driver.quit()
