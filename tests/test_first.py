"""
Smoke test
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

URL = "https://test-shop.qa.studio/"

def test_product_view_sku():
    """
    Test case WERT-2
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # open Browser in maximized mode
    chrome_options.add_argument("--disable-infobars") # disabling infobars
    chrome_options.add_argument("--disable-extensions") # disabling extensions
    chrome_options.add_argument("--disable-gpu") #  applicable to windows os only
    chrome_options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
    # chrome_options.add_argument("--headless")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url=URL)

    tab_best_active = driver.find_element(by=By.CSS_SELECTOR, value="[class*='tab-featured']")
    tab_best_active.click()

    element = driver.find_element(by=By.CSS_SELECTOR, value='[class*="post-11333"]')
    element.click()

    sku = driver.find_element(By.CLASS_NAME, value="sku")
    assert sku.text == '4XAVRC36', "Unexpected sku"

@pytest.mark.smoke
def test_smoke(browser):
    """
    Test case SMK-1
    """
    browser.get(url=URL)
    assert browser.current_url == URL, 'Unexpected URL'
