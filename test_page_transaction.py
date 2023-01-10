import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_transaction():

    @pytest.mark.regression
    def test_transaction_page(self, browser, test_auth):
        test_auth.get(browser)
        transaction_page = browser.find_element(By.XPATH, '/html/body/div/div[2]/div/ul[2]/li[1]/a/p')
        transaction_page.click()

    @pytest.mark.smoke
    def test_text_page(self, browser, test_auth):
        test_auth.get(browser)
        transaction = browser.find_element(By.CLASS_NAME, 'navbar-brand')
        assert transaction == 'Транзакции', "Произошла ошибка"

    @pytest.mark.smoke
    def test_text_button(self, browser, test_auth):
        test_auth.get(browser)
        
        transaction_filter = browser.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[3]/table/thead/tr/th[1]/div/span[2]/span[1]/i')
        transaction_filter.click()

        button_text = browser.find_element(By.XPATH, '//*[@id="el-popover-4736"]/div[1]/button/span')
        assert button_text == 'Применить', "текст не соотвествует ОР"