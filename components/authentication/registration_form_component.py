from components.base_component import BaseComponent
from playwright.sync_api import Page
import allure
from elements.input import Input


class RegistrationFormComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)
        self.field_email = Input(page, "registration-form-email-input", "Email")
        self.field_username = Input(page, "registration-form-username-input", "Username")
        self.field_password = Input(page, "registration-form-password-input", "Password")

    @allure.step("Fill registration form")
    def fill(self, email: str, username: str, password: str):
        self.field_email.fill_manual_emulation(email)
        self.field_email.check_have_value(email)

        self.field_username.fill_manual_emulation(username)
        self.field_username.check_have_value(username)

        self.field_password.fill_manual_emulation(password)
        self.field_password.check_have_value(password)

    @allure.step("Check visible registration form")
    def check_visible(self, email: str = "", username: str = "", password: str = ""):
        self.field_email.check_visible()
        self.field_email.check_have_value(email)

        self.field_username.check_visible()
        self.field_username.check_have_value(username)

        self.field_password.check_visible()
        self.field_password.check_have_value(password)
