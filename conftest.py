import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://release-tkp-lko.secgw.ru/"

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(30)
    browser.quit()

@pytest.fixture
def test_auth():
    login = browser.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/input')
    login.send_keys("admin")
    password = browser.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/input')
    password.send_keys("123")
    button = browser.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div/div/div/div[2]/div[3]/button[1]')
    button.click()