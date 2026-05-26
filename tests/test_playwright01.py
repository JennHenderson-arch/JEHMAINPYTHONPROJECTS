import time

from playwright.sync_api import expect


def test_example_title(browser_type) -> None:
    # Launch headed so you can see the browser when running from Test Explorer
    browser = browser_type.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    time.sleep(5)  # Just to see the page before it closes
    expect(page).to_have_title("Example Domain")
    browser.close()
