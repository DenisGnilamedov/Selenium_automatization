link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")


# pytest -v --tb=line --reruns 1 test_3_6_step7_rerun_test.py

# "--reruns n", где n — это количество перезапусков.
#  "--tb=line" - сократить лог с результатами теста.