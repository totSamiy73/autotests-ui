from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    field_email = page.get_by_test_id("registration-form-email-input").locator("input")
    field_email.press_sequentially("user.name@gmail.com", delay=100)
    field_username = page.get_by_test_id("registration-form-username-input").locator("input")
    field_username.press_sequentially("username", delay=100)
    field_password = page.get_by_test_id("registration-form-password-input").locator("input")
    field_password.press_sequentially("password", delay=100)
    button_registration = page.get_by_test_id("registration-page-registration-button")
    button_registration.click()

    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    headline_courses = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(headline_courses).to_be_visible()
    expect(headline_courses).to_have_text("Courses")

    icon_folder = page.get_by_test_id("courses-list-empty-view-icon")
    expect(icon_folder).to_be_visible()

    text_no_results = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(text_no_results).to_be_visible()
    expect(text_no_results).to_have_text("There is no results")

    text_load_test_pipeline = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(text_load_test_pipeline).to_be_visible()
    expect(text_load_test_pipeline).to_have_text("Results from the load test pipeline will be displayed here")
