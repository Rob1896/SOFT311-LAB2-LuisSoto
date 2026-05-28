from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_cart(self, product_alt: str):
        # Encuentra al producto por su atributo alt en la imagen
        product_image = self.page.locator(f'img[alt="{product_alt}"]')
        product_container = product_image.locator("xpath=..")
        add_button = product_container.locator('button[data-testid="all-products-cart-button"]').first
        add_button.click()

        #ir al carrito
    def go_to_cart(self):
        self.page.locator('[data-testid="header-cart-icon"]').click()
        
        #regresar a la página de productos
    def go_to_products(self):
        self.page.goto("https://storedemo.testdino.com/products", wait_until="domcontentloaded")

