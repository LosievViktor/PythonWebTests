from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.locators import Locators
from pages.strings import Strings


class FileUploadPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def _i_frame(self):
        return self.page.frame_locator(Locators.i_frame)

    @property
    def _file_input(self):
        return self._i_frame.locator(Locators.input_file)

    def upload(self, file_path: str) -> None:
        expect(self._file_input).to_be_attached()
        self._file_input.set_input_files(file_path)

    def assert_uploaded(self) -> None:
        expect(self._i_frame.locator("p", has_text=Strings.MESSAGE_OF_UPLOAD)).to_be_visible()
