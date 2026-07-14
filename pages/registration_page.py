from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.field_email = page.get_by_test_id("registration-form-email-input").locator("input")
        self.field_username = page.get_by_test_id("registration-form-username-input").locator("input")
        self.field_password = page.get_by_test_id("registration-form-password-input").locator("input")
        self.button_registration = page.get_by_test_id("registration-page-registration-button")
        self.login_link = page.get_by_test_id("registration-page-login-link")

    def fill_registration_form(self, email: str, username: str, password: str):
        self.field_email.press_sequentially(email, delay=100)
        expect(self.field_email).to_have_value(email)

        self.field_username.press_sequentially(username, delay=100)
        expect(self.field_username).to_have_value(username)

        self.field_password.press_sequentially(password, delay=100)
        expect(self.field_password).to_have_value(password)

    def click_registration_button(self):
        self.button_registration.click()
