import pytest
from playwright.sync_api import Page, expect

from pages.strings import LINKS, Strings


@pytest.mark.parametrize("page_name", LINKS)
def test_main_page_links(load_page, page_name):
    """This test goes to the web site and visits each chapter link."""
    load_page(page_name)


def test_main_page_attributes(page: Page, load_main_page):
    """This test checks the main page Title."""
    load_main_page()
    expect(page).to_have_title(Strings.PAGE_TITLE)
