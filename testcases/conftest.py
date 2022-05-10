import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def setup(request):
    driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
    driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
