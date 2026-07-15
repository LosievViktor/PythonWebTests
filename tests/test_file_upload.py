import os

from pages.strings import Strings


def test_upload_file_drag_and_drop(load_page, file_upload_page):
    """This test goes to the web site and tests File Upload via Drag and Drop."""
    load_page(Strings.FILE_UPLOAD)

    file_path = os.path.join(os.path.dirname(__file__), "..", "resources", "file.txt")
    file_upload_page.upload(file_path)
    file_upload_page.assert_uploaded()
