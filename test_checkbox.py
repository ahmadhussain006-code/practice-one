
# In this program I clicked on radio button and on the checkbox. Also check the validation using if nd else condition

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    # used - Xpath- //tagline[@attribute='value']
    radioButton = page.wait_for_selector('//input[@value="FeMale"]')
    radioButton.click()
    #page.wait_for_selector('//input[@value="Movies"]').click()
    if radioButton.is_checked():
        print('This is passed')
    else:
        print('This is failed')

    checkBox = page.wait_for_selector('//input[@value="Movies"]')
    checkBox.click()
    if checkBox.is_checked():
        print('This is passed wah')
    else:
        print('This is failed')
    page.wait_for_timeout(3000)