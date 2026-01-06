from playwright.sync_api import sync_playwright, Page

def test_mane_page(page:Page):
    page.goto("https://aqa-proka4.org/sandbox/web")
    assert page.title() == "WEB Sandbox - Практика автоматизации"