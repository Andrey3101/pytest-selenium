from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


link = "https://release-tkp-lko.secgw.ru/"

class Test_authorization():

    def __init__(self):
        pass

    @pytest.fixture
    def test_browse(self):
        browser = webdriver.Chrome()
        browser.get(link)
        yield browser
        time.sleep(30)
        browser.quit()

    @pytest.fixture
    def test_auth(test_browse):
        browse = test_browse.browser
        login = browse.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/input')
        login.send_keys("admin")
        password = browse.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/input')
        password.send_keys("123")
        button = browse.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div/div/div/div[2]/div[3]/button[1]')
        button.click()

    def test_assert_main_page(test_browse):
        browser = test_browse.browser
        page = browser.find_element(By.CLASS_NAME, 'navbar-brand')
        assert page == 'Главная страница', "Произошла ошибка"