import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def time_func(x):
    return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', [
                                f"https://stepik.org/lesson/236895/step/1",
                                f"https://stepik.org/lesson/236896/step/1",
                                f"https://stepik.org/lesson/236897/step/1",
                                f"https://stepik.org/lesson/236898/step/1",
                                f"https://stepik.org/lesson/236899/step/1",
                                f"https://stepik.org/lesson/236903/step/1",
                                f"https://stepik.org/lesson/236904/step/1",
                                f"https://stepik.org/lesson/236905/step/1"])
def test_open_page_and_input_answer(browser, link):
    url = {link}
    browser.get(link)
    browser.implicitly_wait(3)
    x = time.time()
    answer = time_func(x)
    input1 = browser.find_element(By.CLASS_NAME, 'ember-text-area')
    input1.send_keys(str(answer))
    button = browser.find_element(By.CLASS_NAME, 'submit-submission')
    button.click()
    elem_appeared = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
    )
    correct = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    assert correct == "Correct!", "Messages do not correspond"
    print(correct)
