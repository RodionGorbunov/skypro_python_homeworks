# открываем страницу в браузере Chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
Add_Element = "//button[contains(text(), 'Add Element')]"
button = driver.find_element(By.XPATH, Add_Element)

# пять раз кликнуть на кнопку Add Element

for x in range(5):
    button.click()
    sleep(1)
sleep(5)

# собрать со страницы список кнопок Delete

delete_button = driver.find_elements(By.XPATH, '//button[contains(text(), "Delete")]')

# вывести на экран размер списка

print(f"Размер списка, {len(delete_button)}")
driver.quit()

# открываем страницу в браузере Firefox

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
Add_Element = "//button[contains(text(), 'Add Element')]"
button = driver.find_element(By.XPATH, Add_Element)

# пять раз кликнуть на кнопку Add Element

for x in range(5):
    button.click()
    sleep(1)
sleep(5)

# собрать со страницы список кнопок Delete

delete_button = driver.find_elements(By.XPATH, '//button[contains(text(), "Delete")]')

# вывести на экран размер списка

print(f"Размер списка, {len(delete_button)}")
driver.quit()
