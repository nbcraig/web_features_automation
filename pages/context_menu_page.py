from pages.shared_page_components import CommonOps
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class ContextMenu(CommonOps):
    
    # Page element locators
    CONTEXT_MENU_LINK = (By.LINK_TEXT, 'Context Menu')
    CONTEXT_BOX = (By.ID, 'hot-spot')
    PAGE_TITLE = (By.XPATH, '//div[@class="example"]/h3')

    def navigate_to_context_menu_page(self):
        self.wait_for(self.CONTEXT_MENU_LINK).click()

    def right_click_context_menu(self):
        context_menu = self.find(self.CONTEXT_BOX)
        self._action.context_click(context_menu).perform()

    def alert(self):
        self._wait.until(ec.alert_is_present())

    def get_alert_message(self):
        return self._alert.text

    def accept_alert(self):
        self._alert.accept()

    def alert_is_accepted(self):
        return self.find(self.PAGE_TITLE).text