from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, "q")
    SEARCH_BUTTON = (By.CLASS_NAME, "search-box__button--1oH7")

    def search_item(self, item_name):
        search_box = self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        search_box.clear()
        search_box.send_keys(item_name)
        self.click(self.SEARCH_BUTTON)
