from pages.dashboard.dashboard_page import DashboardPage
import pytest
import allure
from tools.allure.tags import AllureTag
from tools.allure.features import AllureFeature
from tools.allure.epics import AllureEpic
from tools.allure.stories import AlluresStory
from allure_commons.types import Severity


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AlluresStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AlluresStory.DASHBOARD)
@allure.tag(AllureTag.DASHBOARD, AllureTag.REGRESSION)
@pytest.mark.dashboard
@pytest.mark.regression
class TestDashboard:

    @allure.severity(Severity.NORMAL)
    @allure.title("Check displaying of dashboard page")
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.vizit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

        dashboard_page_with_state.navbar.check_visible('username')
        dashboard_page_with_state.sidebar.check_visible()

        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        dashboard_page_with_state.check_visible_students_chart()
        dashboard_page_with_state.check_visible_activities_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_scores_chart()
