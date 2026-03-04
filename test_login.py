from playwright.sync_api import sync_playwright

def test_loginPage():

 with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
 #used css locator - tagname[attribute='value']
    usernamefield = page.wait_for_selector('input[name="username"]')
    usernamefield.type('Admin')
 #used css locator - tagname[attribute='value']
    usernamepassword = page.wait_for_selector('input[type="password"]')
    usernamepassword.type('admin123')
 #used css locator - tagname[attribute='value']
    submit = page.wait_for_selector('button[type="submit"]')
    submit.click()
    page.wait_for_timeout(9000)

