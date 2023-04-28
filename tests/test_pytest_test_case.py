
from selenium.common.exceptions import NoSuchElementException
from pages.add_remove_element_page import AddRemoveElementPage
from pages.context_menu_page import ContextMenu
from pages.form_authentication_page import FormAuthPage

# Test for form authentication page
def test_form_authentication(driver):
    instance = FormAuthPage(driver)

    instance.navigate_to_form_page()
    instance.enter_username('tomsmith')
    instance.enter_password('SuperSecretPassword!')
    instance.click_login_button()

    assert 'logged into' in instance.check_login_logout_status().text

    instance.click_logout_btn()
    assert 'logged out' in instance.check_login_logout_status().text


# Test for Add/Remove element page
def test_add_remove_element(driver):
    instance = AddRemoveElementPage(driver)

    instance.navigate_to_add_remove_element_page()
    instance.click_add_element_button()
    try:
        instance.check_delete_button_exists()
    except NoSuchElementException:
        assert False
    assert True
      

# Tests for context menu page
def test_context_menu(driver):
    instance = ContextMenu(driver)

    instance.navigate_to_context_menu_page()
    instance.right_click_context_menu()

    assert 'You selected a context menu' in instance.get_alert_message()

    instance.accept_alert()

    assert 'Context Menu' in instance.alert_is_accepted()
