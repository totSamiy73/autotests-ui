from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage, CheckVisibleCourseCardParams
import pytest
import allure
from tools.allure.tags import AllureTag
from tools.allure.features import AllureFeature
from tools.allure.epics import AllureEpic
from tools.allure.stories import AlluresStory
from allure_commons.types import Severity


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AlluresStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AlluresStory.COURSES)
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@pytest.mark.courses
@pytest.mark.regression
class TestCourses:

    @allure.severity(Severity.NORMAL)
    @allure.title("Check displaying of empty courses list")
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.vizit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.severity(Severity.CRITICAL)
    @allure.title("Create course")
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.vizit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.course_toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.form.check_visible(
            title="",
            description="",
            estimated_time="",
            max_score="0",
            min_score="0")
        create_course_page.exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.course_toolbar_view.check_visible(is_create_course_disabled=False)
        create_course_page.course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(CheckVisibleCourseCardParams(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        ))

    @allure.severity(Severity.NORMAL)
    @allure.title("Create and edit course")
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.vizit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.course_toolbar_view.check_visible(is_create_course_disabled=False)
        create_course_page.course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(CheckVisibleCourseCardParams(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        ))

        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.form.fill(
            title="test edit",
            estimated_time="1 hour",
            description="edit course",
            max_score="10",
            min_score="1"
        )
        create_course_page.course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(CheckVisibleCourseCardParams(
            index=0,
            title="test edit",
            max_score="10",
            min_score="1",
            estimated_time="1 hour"
        ))
