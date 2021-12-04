import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")


# pytest -s -v -m smoke test_3_5_step2_fixture_marks.py
# pytest -s -v -m "not smoke" test_3_5_step2_fixture_marks.py
# pytest -s -v -m "smoke or regression" test_3_5_step2_fixture_marks.py
# pytest -s -v -m "smoke and win10" test_3_5_step2_fixture_marks.py

# Если запустить PyTest с параметром -v (verbose, то есть подробный),
# то в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения

# -s, чтобы увидеть текст, который выводится командой print()

# Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку