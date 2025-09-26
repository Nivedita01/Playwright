from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False, slow_mo=500)  # Set headless=True for headless mode
    # Create a new browser page
    page = browser.new_page()
    # Navigate to a webpage
    page.goto("https://bootswatch.com/default")

    page.get_by_role('button', name='Block button').highlight()
    first_button = page.get_by_role('button', name='Block button').first
    
    page.locator("footer").highlight()
    first_button.click()
    first_button.dblclick(delay=1000)
    first_button.click(button='right')
    first_button.click(modifiers=['Shift']
                       )
    outline_button = page.locator("button.btn-outline-primary")
    outline_button.hover()

    browser.close()
