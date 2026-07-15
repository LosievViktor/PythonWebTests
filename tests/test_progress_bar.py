import time

from pages.strings import Strings


def test_progress_bar(load_page, progress_bar_page):
    """This test goes to the web site and tests the Progress Bar."""
    load_page(Strings.PROGRESS_BAR)

    progress_bar_page.start_button.click()

    while progress_bar_page.get_value_of_progress_bar() < 75:
        time.sleep(0.05)

    progress_bar_page.stop_button.click()

    assert progress_bar_page.get_value_of_progress_bar() == 75
