
#How to select the dropdown text
from playwright.sync_api import sync_playwright

def test_dropdown():
 with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
   #used - Xpath- //tagline[@attribute='value']
    #dropdown = page.select_option('//select[@id="Skills"]',label="Art Design")
   # dropdown.select_option(label='Art Design')
    page.wait_for_timeout(5000)
    dropdown = page.query_selector('//select[@id="Skills"]')
    dropdown.select_option(label='Backup Management')