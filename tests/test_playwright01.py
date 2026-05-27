#20260625 - JEH updated to pull CI ststus and run headless. Else for debug local runs it will run with headed browser and pause for 5 seconds to allow for visual confirmation of the test running. This is a simple test that checks if the title of the Google homepage is "Google". It uses Playwright's expect API to assert the title and includes a debug pause that only activates when not running in a CI environment. "is_ci" is on conftest.py  

import time

from playwright.sync_api import expect


""" def test_example_title(browser_type, is_ci):
    browser = browser_type.launch(headless=is_ci)
    page = browser.new_page()
    page.goto("https://example.com")

    time.sleep(5)

    expect(page).to_have_title("Example Domain")
    print("Title is correct.")
    browser.close() """

def test_example_title(page, is_ci):
    page.goto("https://example.com")
    time.sleep(5)
    expect(page).to_have_title("Example Domain")
    print("Title is correct.")
    #page.close()  #this causes page to close before the page title can be checked.  I think it is because the page object is shared across tests, so closing it here would affect other tests that use the same page. By not closing it, we allow the test to check the title before any cleanup happens. The browser will still be closed at the end of the test session by Playwright's test runner, so we don't need to worry about leaving it open.
 