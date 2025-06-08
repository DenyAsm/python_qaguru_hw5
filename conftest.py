import pytest
from selene import have, browser

@pytest.fixture(scope = "function")
def demo_qa():
    #browser.config.driver_name = 'edge' # список стандартных driver_name: chrome, firefox, edge, remote, appium
    browser.driver.maximize_window() # Максимизация окна браузера
    #browser.config.window_width = 1200
    #browser.config.window_height = 800
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.open('/') # если прокинул конфиг браузера по base_url, тогда можно будет написать так '/'
    browser.config.timeout = 10 # время ожидания в секундах (по дефолту в Selene 4 сек)
    #browser.should(have.script_returned(True, 'return document.readyState === "complete"'))
    yield
    browser.quit()