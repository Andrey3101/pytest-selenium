import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_auth import Test_authorization

class Test_transaction():

    def __init__(self):
        pass

    @pytest.fixture
    def test_page(test_browse, test_auth):
        browser = test_browse.browser
        transaction_page = browser.find_element(By.XPATH, '/html/body/div/div[2]/div/ul[2]/li[1]/a/p')
        transaction_page.click()

    def test_text_page(test_browse):
        browser = test_browse.browser
        transaction = browser.find_element(By.CLASS_NAME, 'navbar-brand')
        assert transaction == 'Транзакции', "Произошла ошибка"

    def test_txt_button(test_browse):
        browser = test_browse.browser
        
        transaction_filter = browser.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[3]/table/thead/tr/th[1]/div/span[2]/span[1]/i')
        transaction_filter.click()

        button_text = browser.find_element(By.XPATH, '//*[@id="el-popover-4736"]/div[1]/button/span')
        assert button_text == 'Применить', "текст не соотвествует ОР"