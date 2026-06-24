import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    page.get_by_test_id('login-form-email-input').locator('input').fill("что то")
    page.get_by_test_id('login-form-password-input').locator('input').fill("qweetyy")
    page.get_by_test_id('login-page-login-button').click()
    expect(page.get_by_test_id("login-page-wrong-email-or-password-alert")).to_be_visible()
    expect(page.get_by_test_id("login-page-wrong-email-or-password-alert")).to_have_text("Wrong email or password")
    time.sleep(3)

