from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.ID, 'input_value') # достаем значение х из браузера
x = x_element.text
y = calc(x)
print(y)
answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)
checkbox_click = browser.find_element(By.ID, "robotCheckbox")
checkbox_click.click()
radio_click = browser.find_element(By.ID, "robotsRule")
radio_click.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
browser.quit()