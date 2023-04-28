from pages.shared_page_components import CommonOps
from selenium.webdriver.common.by import By

class FormAuthPage(CommonOps):

    # Web elements locators
    FORM_AUTH_LINK = (By.LINK_TEXT, 'Form Authentication')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.XPATH, '//button[@type="submit"]')
    ALERT = (By.ID, 'flash')
    LOGOUT_BTN = (By.CLASS_NAME, 'button')

    def navigate_to_form_page(self):
        self.wait_for(self.FORM_AUTH_LINK).click()
        
    def enter_username(self, username):
        self.wait_for(self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.find(self.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find(self.LOGIN_BTN).click()

    def click_logout_btn(self):
        self.find(self.LOGOUT_BTN).click()

    def check_login_logout_status(self):
       return  self.wait_for(self.ALERT)