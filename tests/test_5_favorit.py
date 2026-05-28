import sys
from pathlib import Path
import pytest


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pages.addfavorite_page import FavoritePage
from utils import save_screenshot

def test_add_product_to_favorites(page, request):
    favorite_page = FavoritePage(page)
    page.goto("https://storedemo.testdino.com/products", wait_until="domcontentloaded")

    # Agregar 1 producto a favoritos
    favorite_page.add_to_favorites("JBL Charge 4 Bluetooth Speaker")

    # Ir a la página de favoritos
    favorite_page.go_to_favorites()

    # Validar que el producto aparece en la lista de favoritos
    product_in_favorites = page.locator('text="JBL Charge 4 Bluetooth Speaker"')
    assert product_in_favorites.is_visible()
    save_screenshot(page, request, "JBL Charge 4 Bluetooth Speaker")



    # Regresar a la página de productos
    favorite_page.go_to_products()
    assert page.url == "https://storedemo.testdino.com/products"

    #agregar otro producto a favoritos
    favorite_page.add_to_favorites("Rode NT1-A Condenser Mic")
    favorite_page.go_to_favorites()

    product_in_favorites = page.locator('text="Rode NT1-A Condenser Mic"')
    assert product_in_favorites.is_visible()
    save_screenshot(page, request, "Rode NT1-A Condenser Mic")

    favorite_page.go_to_products()
    assert page.url == "https://storedemo.testdino.com/products"






### correr el reporte del HTML y ver los resultados de las preubas con .venv/bin/python -m pytest --html=report.html --self-contained-html

    

