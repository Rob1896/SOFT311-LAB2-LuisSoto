import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pages.signup_page import Signup_page

@pytest.mark.dependency(name="signup")
def test_signup_page(page):
    signup = Signup_page(page)
    page.goto("https://storedemo.testdino.com/login", wait_until="domcontentloaded")
    
    signup.click_signup_button()
    page.wait_for_selector("input[id='firstname']", timeout=5000)

    signup.fill_first_name("Peggymagg")
    signup.fill_last_name("Mosss")
    signup.fill_email("carlos159@example.com")
    signup.fill_password("SecurePassword123!")

    signup.click_create_account_button()
    page.wait_for_url("**", timeout=5000)

    page.wait_for_url("https://storedemo.testdino.com/login", timeout=5000)

    
    assert page.url == "https://storedemo.testdino.com/login"


