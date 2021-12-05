import time
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
    time.sleep(3)

# pytest -s -v --browser_name=firefox test_3_6_step4_diff_browsers.py