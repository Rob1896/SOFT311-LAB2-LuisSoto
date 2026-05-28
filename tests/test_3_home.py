import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pages.home_page import HomePage


def test_home_page(page, request):
    home_page = HomePage(page)
    home_page.open()
    
    # Validate the URL of the home page
    expected_url = "https://storedemo.testdino.com/"
    assert page.url == expected_url, f"Expected URL to be '{expected_url}' but got '{page.url}'"


    test_name = request.node.name.replace("[", "_").replace("]", "_")
    page.screenshot(path=f"screenshots/{test_name}.png", full_page=True)