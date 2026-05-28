import sys
from pathlib import Path
import pytest
import time

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pages.login_page import LoginPage

def test_login(page, request):
    login = LoginPage(page)
    page.goto("https://storedemo.testdino.com/login", wait_until="domcontentloaded")
    
    login.fill_email("RoMS@example.com")
    login.fill_password("SecurePassword123!")
    login.click_submit_button()

    # Esperar a que aparezca el icono del logo en la página post-login
    page.wait_for_selector('[data-testid="header-menu-home"]', timeout=5000)

    # Validar que el logo está visible
    assert page.locator('[data-testid="header-menu-home"]').is_visible()
    time.sleep(3)  # Esperar un momento para asegurarse de que la página se ha cargado completamente


    test_name = request.node.name.replace("[", "_").replace("]", "_")
    page.screenshot(path=f"screenshots/{test_name}.png", full_page=True)


