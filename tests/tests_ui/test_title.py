from playwright.sync_api import Page


def test_mane_page_title(page: Page):
    page.goto("https://aqa-proka4.org/sandbox/web")
    assert page.title() == "WEB Sandbox - Практика автоматизации"