from playwright.sync_api import Page

class FavoritePage:
    def __init__(self, page: Page):
        self.page = page
        self.wishlist_icon = page.locator('[data-testid="header-wishlist-icon"]')

    def add_to_favorites(self, product_alt: str):
        # Encuentra el contenedor que tiene la imagen del producto específico
        product_container = self.page.locator(
            "div",
            has=self.page.locator(f'img[alt="{product_alt}"]')
        )
        # Dentro de ese contenedor, busca el botón de favoritos
        favorite_button = product_container.locator('button[data-testid="all-products-wishlist-button"]')
        favorite_button.first.click()

    def go_to_favorites(self):
        self.wishlist_icon.click()
