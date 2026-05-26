from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.email_input = self.page.locator('input[id="email"]')
        self.password_input = self.page.locator('input[id="password"]')
        self.submit_button = self.page.locator('button[data-testid="login-submit-button"]')
        

        
    def fill_email(self, email):
        self.email_input.fill(email)

    def fill_password(self, password):
        self.password_input.fill(password)
    
    def click_submit_button(self):
        self.submit_button.click()
