from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Index.html')
    # used - #id
    EmailTextBox=page.wait_for_selector('#email')
    EmailTextBox.type('test@test.com')
    ClickButton = page.wait_for_selector('#enterimg')
    ClickButton.click()
    page.wait_for_timeout(3000)