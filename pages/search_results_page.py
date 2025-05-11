from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class SearchResultsPage(BasePage):
    BRAND_FILTER = (By.XPATH, "//label[contains(text(), 'Samsung')]")
    MIN_PRICE = (By.NAME, "min-price")
    MAX_PRICE = (By.NAME, "max-price")
    APPLY_PRICE = (By.XPATH, "//button[.='Apply']")
    PRODUCTS = (By.XPATH, "//div[contains(@class, 'gridItem--Yd0sa')]")
    FIRST_PRODUCT = (By.XPATH, "(//div[contains(@class, 'gridItem--Yd0sa')])[1]")
    RESULT_CONTAINER = (By.CSS_SELECTOR, ".c3gUW0")

    def wait_for_search_results(self):
        self.wait.until(EC.presence_of_element_located(self.RESULT_CONTAINER))

    def apply_brand_filter(self):
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.BRAND_FILTER))
            element.click()
        except TimeoutException:
            self.driver.save_screenshot("brand_filter_timeout.png")
            print("Brand filter not clickable; trying JS click.")
            element = self.driver.find_element(*self.BRAND_FILTER)
            self.driver.execute_script("arguments[0].click();", element)

    def set_price_filter(self, min_price, max_price):
        self.send_keys(self.MIN_PRICE, min_price)
        self.send_keys(self.MAX_PRICE, max_price)
        self.click(self.APPLY_PRICE)

    def get_product_count(self):
        products = self.get_elements(self.PRODUCTS)
        return len(products)

    def click_first_product(self):
        self.click(self.FIRST_PRODUCT)
