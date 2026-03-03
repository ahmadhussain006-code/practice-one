from playwright.sync_api import sync_playwright
with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://demo.automationtesting.in/Alerts.html')
        page.wait_for_selector('//a[@href="#CancelTab"]').click()
        page.wait_for_selector('//div[@id="CancelTab"]').click()
        page.wait_for_timeout(3000)