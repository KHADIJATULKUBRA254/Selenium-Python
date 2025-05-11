import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.mark.usefixtures("setup")
class TestSearch:
    driver: WebDriver

    def test_product_search_count(self):
        home = HomePage(self.driver)
        search = SearchResultsPage(self.driver)

        home.search_item("laptop")
        search.apply_brand_filter()
        search.set_price_filter("500", "5000")
        count = search.get_product_count()

        assert count > 0, "No products found in result"

    def test_free_shipping(self):
        home = HomePage(self.driver)
        search = SearchResultsPage(self.driver)
        product = ProductPage(self.driver)

        home.search_item("laptop")
        search.apply_brand_filter()
        search.set_price_filter("500", "5000")
        search.click_first_product()

        assert product.is_free_shipping_available(), "Free shipping not available"
