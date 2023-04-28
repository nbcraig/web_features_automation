from pages.shared_page_components import CommonOps
from selenium.webdriver.common.by import By

class AddRemoveElementPage(CommonOps):

    # Page locators
    ADD_REMOVE_LINK = (By.LINK_TEXT, 'Add/Remove Elements')
    ADD_ELEMENT_BTN = (By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    DELETE_BTN = (By.CLASS_NAME, 'added-manually')

    def navigate_to_add_remove_element_page(self):
        self.wait_for(self.ADD_REMOVE_LINK).click()

    def click_add_element_button(self):
        self.wait_for(self.ADD_ELEMENT_BTN).click()

    def check_delete_button_exists(self):
        self.find(self.DELETE_BTN)