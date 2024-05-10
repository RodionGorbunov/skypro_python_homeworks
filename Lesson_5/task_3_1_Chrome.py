# открываем страницу в браузере Chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# пять раз кликнуть на кнопку Add Element

for x in range(5):
    driver.find_element(By.XPATH, "//button[contains(text(), 'Add Element')]").click()
    sleep(1)
sleep(5)

# собрать со страницы список кнопок Delete

delete_button = driver.find_elements(By.XPATH, '//button[contains(text(), "Delete")]')

# вывести на экран размер списка

print(f"Размер списка, {len(delete_button)}")
driver.quit()
