from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page


class RegistrationPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.form = RegistrationFormComponent(page)

        self.button_registration = page.get_by_test_id("registration-page-registration-button")
        self.login_link = page.get_by_test_id("registration-page-login-link")

    def click_registration_button(self):
        self.button_registration.click()
