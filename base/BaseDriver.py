class BaseDriver:
    def __init__(self, driver) -> None:
        self.driver = driver

    def find_element(self, *locator: object) -> object:
        return self.driver.find_element(*locator)
