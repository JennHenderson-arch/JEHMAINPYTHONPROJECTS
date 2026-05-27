#test_W3C_SQLtest.py

#https://www.w3schools.com/
#python.exe -m playwright codegen https://www.w3schools.com/ --target=python

import time
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_runSQL(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.w3schools.com/")
    expect(page).to_have_title("W3Schools Online Web Tutorials")
    time.sleep(5)

    page.get_by_role("link", name="SQL", description="SQL Tutorial", exact=True).click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Try it Yourself »").click()
    time.sleep(2)

    page1 = page1_info.value
    page1.get_by_role("cell", name="Employees").click()
    page1.locator("pre").click()
    time.sleep(2)

# Focus the element first
    locator = page1.get_by_role("textbox")
    locator.focus()
# Use Control+A (Windows/Linux) or Meta+A (Mac) then Backspace THIS WORKS!!
    page1.keyboard.press("Control+A") 
    page1.keyboard.press("Backspace")

    time.sleep(2)
    page1.get_by_role("textbox").fill("SELECT * FROM Employees where FirstName= 'Nancy';")
    time.sleep(5)

    page1.get_by_role("button", name="Run SQL »").click()
    time.sleep(5)
    expect(page1.locator("iframe[name=\"view\"]").content_frame.get_by_role("rowgroup")).to_contain_text("Education includes a BA in psychology from Colorado State University. She also completed (The Art of the Cold Call). Nancy is a member of Toastmasters International.")

    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_runSQL(playwright)