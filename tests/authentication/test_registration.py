import allure
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
import pytest
from tools.allure.tags import AllureTag
from tools.allure.features import AllureFeature
from tools.allure.epics import AllureEpic
from tools.allure.stories import AlluresStory
from allure_commons.types import Severity


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AlluresStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AlluresStory.REGISTRATION)
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@pytest.mark.registration
@pytest.mark.regression
class TestRegistration:

    @allure.severity(Severity.CRITICAL)
    @allure.title("Registration with correct email, username, and password")
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.vizit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.form.check_visible()
        registration_page.form.fill("user.name@gmail.com", "username", "password")
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible()
