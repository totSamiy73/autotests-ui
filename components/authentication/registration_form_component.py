from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class RegistrationFormComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)

        self.field_email = page.get_by_test_id("registration-form-email-input").locator("input")
        self.field_username = page.get_by_test_id("registration-form-username-input").locator("input")
        self.field_password = page.get_by_test_id("registration-form-password-input").locator("input")

    def fill(self, email: str, username: str, password: str):
        self.field_email.press_sequentially(email, delay=100)
        expect(self.field_email).to_have_value(email)

        self.field_username.press_sequentially(username, delay=100)
        expect(self.field_username).to_have_value(username)

        self.field_password.press_sequentially(password, delay=100)
        expect(self.field_password).to_have_value(password)

    def check_visible(self, email: str = "", username: str = "", password: str = ""):
        expect(self.field_email).to_be_visible()
        expect(self.field_email).to_have_value(email)

        expect(self.field_username).to_be_visible()
        expect(self.field_username).to_have_value(username)

        expect(self.field_password).to_be_visible()
        expect(self.field_password).to_have_value(password)
