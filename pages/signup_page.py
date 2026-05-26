from playwright.sync_api import Page

class Signup_page:
    def __init__(self, page: Page):
        self.page = page
        self.signup_button = self.page.locator('span[data-testid="login-signup-link"]')
        self.first_name_input = self.page.locator('input[id="firstname"]')
        self.last_name_input = self.page.locator('input[id="lastname"]')
        self.email_input = self.page.locator('input[id="email"]')
        self.password_input = self.page.locator('input[id="password"]')
        self.create_account_button = self.page.locator('button[data-testid="signup-submit-button"]')


    def click_signup_button(self):
        self.signup_button.click()

    def click_create_account_button(self):
        self.create_account_button.click()

    def fill_first_name(self, name):
        self.first_name_input.fill(name)

    def fill_last_name(self, name):
        self.last_name_input.fill(name)

    def fill_email(self, email):
        self.email_input.fill(email)

    def fill_password(self, password):
        self.password_input.fill(password)

    def get_title(self):
        return self.page.title()
    




