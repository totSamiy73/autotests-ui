import re
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
from playwright.sync_api import Page


class RegistrationPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.form = RegistrationFormComponent(page)

        self.button_registration = Button(page, "registration-page-registration-button", "Registration button")
        self.login_link = Link(page, "registration-page-login-link", "Login link")

    def click_registration_button(self):
        self.button_registration.click()

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login"))
