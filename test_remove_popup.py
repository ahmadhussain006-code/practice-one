
#How to click on a alert button

from playwright.sync_api import sync_playwright

def test_radioButton_checkBox():
 with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')
    # used - Xpath- //tagline[@attribute='value']
    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    #page.on("dialog",lambda diolog : diolog.dismiss())
    page.wait_for_selector('//div[@id="CancelTab"]').click()
    page.wait_for_timeout(3000)