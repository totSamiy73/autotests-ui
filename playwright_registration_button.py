from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    button_registration = page.get_by_test_id("registration-page-registration-button")

    expect(button_registration).not_to_be_enabled()

    field_email = page.get_by_test_id("registration-form-email-input").locator("input")
    field_email.press_sequentially("user.name@gmail.com", delay=100)
    field_username = page.get_by_test_id("registration-form-username-input").locator("input")
    field_username.press_sequentially("username", delay=100)
    field_password = page.get_by_test_id("registration-form-password-input").locator("input")
    field_password.press_sequentially("password", delay=100)

    expect(button_registration).to_be_enabled()
