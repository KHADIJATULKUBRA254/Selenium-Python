import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.daraz.pk/")
    request.cls.driver = driver
    yield
    driver.quit()
