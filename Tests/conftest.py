import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://dev-main-master2.vedant.life/en/enquiry-gita")
    request.cls.driver = driver
    yield
    driver.close()

