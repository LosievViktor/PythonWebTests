from playwright.sync_api import expect

from pages.strings import Strings


def test_login_form_positive(load_page, sample_app_page, login, password):
    """This test goes to the web site and tests the login page in the Positive case."""
    load_page(Strings.SAMPLE_APP)

    sample_app_page.login(login, password)

    expect(sample_app_page.status_label).to_have_text(f"{Strings.WELCOME_USER_MESSAGE} {login}!")


def test_login_form_negative(load_page, sample_app_page, login, wrong_password):
    """This test goes to the web site and tests the login page in the Negative case."""
    load_page(Strings.SAMPLE_APP)

    sample_app_page.login(login, wrong_password)

    expect(sample_app_page.status_label).to_have_text(Strings.WRONG_PASSWORD_MESSAGE)
