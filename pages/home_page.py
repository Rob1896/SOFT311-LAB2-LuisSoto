
from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://storedemo.testdino.com/"

    def open(self):
        self.page.goto(self.url)

    def get_title(self):
        return self.page.title()
