from playwright.sync_api import sync_playwright, Page, expect
import pytest

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://aqa-proka4.org/sandbox/web")
    page.screenshot(path="screenshot/homepage.png")
    page.close()
