from elements.base_element import BaseElement
from playwright.sync_api import Locator, expect


class Input(BaseElement):

    def get_locator(self, **kwargs) -> Locator:
        return super().get_locator(**kwargs).locator("input")

    def fill(self, value: str, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)

    def fill_manual_emulation(self, value: str, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.press_sequentially(value, delay=100)
