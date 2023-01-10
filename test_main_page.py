from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest



class Test_authorization():

    @pytest.mark.regression
    def test_assert_main_page(self, browser, test_auth):
        test_auth.get(browser)
        page = browser.find_element(By.CLASS_NAME, 'navbar-brand')
        assert page == 'Главная страница', "Произошла ошибка"