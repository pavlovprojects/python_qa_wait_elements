import pytest
from selenium import webdriver


def driver_factory(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="drivers/geckodriver")
    elif browser == "yandex":
        driver = webdriver.Chrome(executable_path="drivers/yandexdriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path="drivers/operadriver")
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception("Driver not supported")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def browser(request):
    driver = driver_factory(request.config.getoption("--browser"))
    driver.maximize_window()
    # driver.implicitly_wait(5)
    request.addfinalizer(driver.close)
    return driver
