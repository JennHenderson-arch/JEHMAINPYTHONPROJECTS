import time

from playwright.sync_api import expect


def test_google_title(browser_type) -> None:
    browser = browser_type.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    time.sleep(5)  # Just to see the page before it closes
    expect(page).to_have_title("Google")
    browser.close()
