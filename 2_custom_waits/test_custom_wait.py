from selenium.webdriver.support.wait import WebDriverWait

"""
class amount_of_elements_with_name:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __call__(self, driver):
        elements = driver.find_elements(By.CLASS_NAME, self.name)
        if len(elements) == self.amount:
            return elements
        else:
            return False
"""


def test_custom_wait(browser):
    browser.get("http://0.0.0.0:8000")
    button = browser.find_element_by_name("showjsbutton")
    button.click()
    button.click()
    button.click()
    elements = WebDriverWait(browser, 3).until(amount_of_elements_with_name(browser, "target", 3))
    for el in elements:
        el.click()
    elements = WebDriverWait(browser, 2).until(amount_of_elements_with_name(browser, "target", 1))
    elements[0].click()
    WebDriverWait(browser, 5).until(amount_of_elements_with_name(browser, "target", 0))
