import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pages.addproduct_page import ProductPage

def test_add_product_to_cart(page):
    product_page = ProductPage(page)

    page.goto("https://storedemo.testdino.com/products", wait_until="domcontentloaded")

    # Agregar el micrófono al carrito
    product_page.add_to_cart("Rode NT1-A Condenser Mic")
    


    # Validar que aparece en el carrito
    cart_item = page.locator('text="Rode NT1-A Condenser Mic"')
    assert cart_item.is_visible()
