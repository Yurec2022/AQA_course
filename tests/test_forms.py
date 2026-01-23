from playwright.sync_api import expect


def test_main_page_title(page, home, fake_user):
    home.register(**fake_user)
    home.assert_success()


def test_url(page):
    expect(page).to_have_url("https://aqa-proka4.org/sandbox/web")


def test_title(page):
    expect(page).to_have_title("WEB Sandbox - Практика автоматизации")
