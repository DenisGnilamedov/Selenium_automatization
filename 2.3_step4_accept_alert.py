from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)

button1 = browser.find_element(By.CLASS_NAME, "btn")
button1.click()
confirm = browser.switch_to.alert
confirm.accept()
x = browser.find_element(By.ID, "input_value").text
y = calc(x)
answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)
button2 = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
button2.click()

time.sleep(10)
browser.quit()