from playwright.sync_api import expect, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    headline_courses = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(headline_courses).to_be_visible()
    expect(headline_courses).to_have_text("Courses")

    icon_folder = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(icon_folder).to_be_visible()

    text_no_results = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(text_no_results).to_be_visible()
    expect(text_no_results).to_have_text("There is no results")

    text_load_test_pipeline = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(text_load_test_pipeline).to_be_visible()
    expect(text_load_test_pipeline).to_have_text("Results from the load test pipeline will be displayed here")
