import os
import pytest
from playwright.sync_api import Page
from faker import Faker
from pages.home_page import HomePage

fake = Faker()

@pytest.fixture(autouse=True)
def open_sandbox(page: Page, request):
    page.goto("https://aqa-proka4.org/sandbox/web")
    yield page

@pytest.fixture
def home(page: Page):
    return HomePage(page)

@pytest.fixture
def fake_user():
    return {
        "login": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(length=10),
    }