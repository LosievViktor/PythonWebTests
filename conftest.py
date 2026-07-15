import os

import pytest
from playwright.sync_api import expect

from pages.file_upload_page import FileUploadPage
from pages.locators import Locators
from pages.progress_bar_page import ProgressBarPage
from pages.sample_app_page import SampleAppPage

"""
Root fixtures, equivalent to the C# project's BaseTest class plus its
TestContext.Parameters (sourced from live.runsettings).

Parameters can be overridden either via environment variables or via
pytest command-line options, e.g.:

    ENVIRONMENT=http://uitestingplayground.com/ pytest
    pytest --login=Viktor --password=pwd --wrong-password=pwd123
"""


def pytest_addoption(parser):
    parser.addoption("--login", action="store", default=os.environ.get("LOGIN", "Viktor"),
                      help="Login used by the Sample App tests")
    parser.addoption("--password", action="store", default=os.environ.get("PASSWORD", "pwd"),
                      help="Password used by the Sample App positive-case test")
    parser.addoption("--wrong-password", action="store", default=os.environ.get("WRONG_PASSWORD", "pwd123"),
                      help="Password used by the Sample App negative-case test")


@pytest.fixture(scope="session")
def base_url():
    # pytest-playwright uses this fixture to resolve relative page.goto() calls.
    return os.environ.get("ENVIRONMENT", "http://uitestingplayground.com/")


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    headless = os.environ.get("HEADLESS", "false").lower() == "true"
    return {**browser_type_launch_args, "headless": headless}


@pytest.fixture
def login(request):
    return request.config.getoption("--login")


@pytest.fixture
def password(request):
    return request.config.getoption("--password")


@pytest.fixture
def wrong_password(request):
    return request.config.getoption("--wrong-password")


@pytest.fixture
def load_main_page(page, base_url):
    def _load():
        page.goto(base_url)

    return _load


@pytest.fixture
def load_page(page, base_url):
    def _load(chapter: str):
        page.goto(base_url)
        page.get_by_role("link", name=chapter).click()
        expect(page.locator(Locators.header_tag)).to_have_text(chapter)

    return _load


@pytest.fixture
def sample_app_page(page):
    return SampleAppPage(page)


@pytest.fixture
def progress_bar_page(page):
    return ProgressBarPage(page)


@pytest.fixture
def file_upload_page(page):
    return FileUploadPage(page)
