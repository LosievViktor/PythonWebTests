from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.locators import Locators


class SampleAppPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def _login_text_field(self):
        return self.page.locator(Locators.txt_login)

    @property
    def _password_text_field(self):
        return self.page.locator(Locators.txt_password)

    @property
    def _login_button(self):
        return self.page.locator(Locators.btn_login)

    @property
    def status_label(self):
        return self.page.locator(Locators.lbl_status)

    def login(self, user: str, password: str) -> None:
        self._login_text_field.fill(user)
        self._password_text_field.fill(password)
        self._login_button.click()
