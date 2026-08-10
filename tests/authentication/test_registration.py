from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
import pytest


@pytest.mark.registration
@pytest.mark.regression
class TestRegistration:

    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.vizit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.form.check_visible()
        registration_page.form.fill("user.name@gmail.com", "username", "password")
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible()
