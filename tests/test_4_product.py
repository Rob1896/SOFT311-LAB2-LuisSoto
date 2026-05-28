import sys
from pathlib import Path
import pytest
import time


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pages.addproduct_page import ProductPage
from utils import save_screenshot

def test_add_product_to_cart(page, request):
    product_page = ProductPage(page)
    page.goto("https://storedemo.testdino.com/products", wait_until="domcontentloaded")

    # Agregar producto al carrito
    product_page.add_to_cart("Rode NT1-A Condenser Mic")
    product_page.go_to_cart()
    product_in_cart = page.locator('text="Rode NT1-A Condenser Mic"')
    assert product_in_cart.is_visible()
    save_screenshot(page, request, "Rode")

    # Regresar a la página de productos
    product_page.go_to_products()
    assert page.url == "https://storedemo.testdino.com/products"

    # Agregar segundo producto al carrito
    product_page.add_to_cart("Seagate 4TB External Hard Drive")
    product_page.go_to_cart()
    product_in_cart = page.locator('text="Seagate 4TB External Hard Drive"')
    assert product_in_cart.is_visible()
    save_screenshot(page, request, "Seagate")

    # Regresar a la página de productos
    product_page.go_to_products()
    assert page.url == "https://storedemo.testdino.com/products"
