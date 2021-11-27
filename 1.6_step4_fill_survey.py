from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input") # input
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name") # [name="last_name"]
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city") # .city
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country") # #country
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn") # button.btn
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()