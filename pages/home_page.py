from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page


class HomePage(BasePage):

    #Locators

    @property
    def input_login(self):
        return self.page.locator('//*[@id="username"]')

    @property
    def input_email(self):
        return self.page.locator('//*[@id="email"]')

    @property
    def input_password(self):
        return self.page.locator('//*[@id="password"]')

    @property
    def pick_country(self):
        return self.page.locator('//*[@id="country"]')

    @property
    def checkbox_terms(self):
        return self.page.locator('//*[@id="terms"]')

    @property
    def button_register(self):
        return self.page.get_by_role("button", name="Register")

    @property
    def result(self):
        return self.page.locator('//*[@id="formResult"]')

    #Actions

    def register(self, login: str, email: str, password: str):
        self.input_login.fill(login)
        self.input_email.fill(email)
        self.input_password.fill(password)

        self.pick_country.click()
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        self.checkbox_terms.click()
        self.button_register.click()

    #Asserts

    def assert_success(self):
        expect(self.result).to_contain_text("Форма успешно")
