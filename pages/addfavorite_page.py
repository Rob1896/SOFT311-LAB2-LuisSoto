from playwright.sync_api import Page


class FavoritePage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_favorites(self, product_alt: str):
        # Encuentra la imagen del producto
        product_image = self.page.locator(f'img[alt="{product_alt}"]')

        # Sube al contenedor padre del producto
        product_container = product_image.locator("xpath=..")

        # Dentro de ese contenedor, busca el botón de favoritos
        favorite_button = product_container.locator('button[data-testid="all-products-wishlist-button"]').first
        favorite_button.click()

    def go_to_favorites(self):
        # Click en el ícono del header que lleva a favoritos
        self.page.locator('[data-testid="header-wishlist-icon"]').click()

    def go_to_products(self):
        # Regresar a la página de productos
        self.page.goto("https://storedemo.testdino.com/products", wait_until="domcontentloaded")