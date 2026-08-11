import pytest
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import allure
from tools.allure.tags import AllureTag
from tools.allure.features import AllureFeature
from tools.allure.epics import AllureEpic
from tools.allure.stories import AlluresStory
from allure_commons.types import Severity


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AlluresStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AlluresStory.AUTHORIZATION)
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:

    @allure.severity(Severity.BLOCKER)
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with correct email and password")
    def test_successful_authorization(self, registration_page: RegistrationPage, dashboard_page: DashboardPage,
                                      login_page: LoginPage):
        registration_page.vizit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.form.check_visible()
        registration_page.form.fill(email="test@test.com", username="test", password="password")
        registration_page.button_registration.click()

        dashboard_page.navbar.check_visible(username="test")
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.form.check_visible()
        login_page.form.fill(email="test@test.com", password="password")
        login_page.login_button.click()

        dashboard_page.navbar.check_visible(username="test")
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.sidebar.check_visible()

    @allure.severity(Severity.CRITICAL)
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with wrong email or password")
    @pytest.mark.parametrize("email, password",
                             [("user.name@gmail.com", "password"), ("user.name@gmail.com", "  "), ("  ", "password")])
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.vizit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.form.check_visible()
        login_page.form.fill(email, password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTag.NAVIGATION)
    @allure.title("Navigation from login page to registration page")
    def test_navigate_from_authorization(self, login_page: LoginPage, registration_page: RegistrationPage):
        login_page.vizit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.form.check_visible()
        login_page.registration_link.check_visible()
        login_page.click_registration_link()
        registration_page.form.check_visible()
