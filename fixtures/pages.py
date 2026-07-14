from pages.login_page import LoginPage
import pytest
from playwright.sync_api import Page


@pytest.fixture()
def login_page(chromium_page: Page) -> LoginPage:
    obj = LoginPage(chromium_page)
    return obj
