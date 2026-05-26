import sys
from pathlib import Path
import pytest

# Agregar la carpeta raíz al sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pages.addfavorite_page import FavoritePage

def test_add_product_to_favorites(page):
    favorite_page = FavoritePage(page)

    # Ir a la página de productos
    page.goto("https://storedemo.testdino.com/products", wait_until="domcontentloaded")

    # Agregar el micrófono a favoritos
    favorite_page.add_to_favorites("Rode NT1-A Condenser Mic")

    # Ir a la página de favoritos usando el ícono del header
    favorite_page.go_to_favorites()

    # Validar que el producto aparece en la lista de favoritos
    product_in_favorites = page.locator('text="Rode NT1-A Condenser Mic"')
    assert product_in_favorites.is_visible()
