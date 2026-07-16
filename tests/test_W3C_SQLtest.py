#test_W3C_SQLtest.py
#Created by Jennifer E. Henderson 20260625 

#python.exe -m playwright codegen https://www.w3schools.com/ --target=python
#This scrript was largely created with codgen python. I then added some expect statements and a few other tweaks.  It is a simple test that goes to w3schools, clicks on the SQL tutorial, opens the Try it Yourself editor, replaces the default SQL code with a new query, runs it, and checks that the expected result is displayed in the output frame. It uses Playwright's expect API to assert the page title and the content of the output frame, and includes time.sleep() calls to allow for visual confirmation of the test running.

import time
import re
import pytest


from playwright.sync_api import Playwright, expect

@pytest.mark.smoke
@pytest.mark.regression


def test_runSQL(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True) #CI version comment out for debug local runs
    #browser = playwright.chromium.launch(headless=False) #uncomment for debug local runs
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.w3schools.com/")
    expect(page).to_have_title("W3Schools Online Web Tutorials")
    time.sleep(5)

    page.get_by_role("link", name="SQL", description="SQL Tutorial", exact=True).click()
    expect(page).to_have_title("SQL Tutorial") 
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Try it Yourself »").click()
       
    time.sleep(2)

    page1 = page1_info.value
    expect(page1).to_have_title("SQL Tryit Editor v1.6")  
    page1.get_by_role("cell", name="Employees").click()
    page1.locator("pre").click()
    time.sleep(2)


## Clear the wonky textbox that doesn't clear with the normal .clear() method.  
# Focus the element first
    locator = page1.get_by_role("textbox")
    locator.focus()
# Use Control+A then Backspace THIS WORKS!!
    page1.keyboard.press("Control+A") 
    page1.keyboard.press("Backspace")
    time.sleep(2)


    page1.get_by_role("textbox").fill("SELECT * FROM Employees where FirstName= 'Nancy';")
    time.sleep(3)

    page1.get_by_role("button", name="Run SQL »").click()
    time.sleep(2)
    expect(page1.locator("iframe[name=\"view\"]").content_frame.get_by_role("rowgroup")).to_contain_text("Education includes a BA in psychology from Colorado State University. She also completed (The Art of the Cold Call). Nancy is a member of Toastmasters International.")

    print("Expected text is displayed in the output frame.")

    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()

## If you don't comment out the with sync_playwright() as playwright: block, it will run the test immediately every time you save it. By including this block, you can control when the test runs and ensure that it only executes when you want it to. This is especially useful if you want to import this test function into another script or test suite without automatically running it. You can simply call the test_runSQL function from your test suite, and it will execute the test as part of your overall testing process.
# with sync_playwright() as playwright:
#     test_runSQL(playwright)