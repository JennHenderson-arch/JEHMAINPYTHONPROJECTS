import time

from playwright.sync_api import expect


def test_example_title(browser_type, is_ci):
    browser = browser_type.launch(headless=is_ci)
    page = browser.new_page()
    page.goto("https://example.com")

    time.sleep(5)

    expect(page).to_have_title("Example Domain")
    print("Title is correct.")
    browser.close()
 