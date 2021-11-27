import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)
input1 = browser.find_element(By.NAME, 'firstname')
input1.send_keys("Ricardo")
input2 = browser.find_element(By.NAME, 'lastname')
input2.send_keys("Milos")
input2 = browser.find_element(By.NAME, 'email')
input2.send_keys("rMilos@g.com")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла
file = browser.find_element(By.ID, 'file')
file.send_keys(file_path)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()


time.sleep(10)
browser.quit()