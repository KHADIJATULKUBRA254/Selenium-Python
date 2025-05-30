from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
