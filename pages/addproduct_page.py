from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_cart(self, product_alt: str):
        # Encuentra el contenedor que tiene la imagen del producto
        product_container = self.page.locator(
            "div",
            has=self.page.locator(f'img[alt="{product_alt}"]')
        )
        # Dentro del contenedor, busca el botón Add to cart
        add_button = product_container.locator('button[data-testid="all-products-cart-button"]')
        add_button.first.click()   
