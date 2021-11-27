from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.ID, 'treasure') # находим элемент, где спрятан х
x = x_element.get_attribute("valuex")
y = calc(x)
print(x)

answer = browser.find_element(By.ID, "answer")
a = answer.get_attribute("type")
print(a)
answer.send_keys(y)
checkbox_click = browser.find_element(By.ID, "robotCheckbox")
checkbox_click.click()
radio_click = browser.find_element(By.ID, "robotsRule")
radio_click.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
browser.quit()