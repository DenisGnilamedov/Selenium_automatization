from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_has_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    basket_but = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert basket_but, "Button not found!"