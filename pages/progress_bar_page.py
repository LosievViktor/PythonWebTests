from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.locators import Locators


class ProgressBarPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def start_button(self):
        return self.page.locator(Locators.btn_start)

    @property
    def stop_button(self):
        return self.page.locator(Locators.btn_stop)

    @property
    def _bar(self):
        return self.page.locator(Locators.progress_bar)

    def get_value_of_progress_bar(self) -> int:
        value = self._bar.get_attribute(Locators.progress_bar_value)
        return int(value) if value is not None else 0
