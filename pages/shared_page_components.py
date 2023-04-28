from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

class CommonOps:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)
        self._action = ActionChains(self.driver)
        self._alert = Alert(self.driver)

    def wait_for(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))
    
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def context_click(self, element):
        return self._action.context_click(element)