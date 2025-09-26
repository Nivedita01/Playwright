from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False, slow_mo=500)  # Set headless=True for headless mode
    # Create a new browser page
    page = browser.new_page()
    # Navigate to a webpage
    page.goto("https://bootswatch.com/default")

    page.get_by_label('Email address').highlight()    
    page.locator("footer").highlight()
    page.get_by_placeholder('Enter email').highlight()
    page.locator("footer").highlight()
    input = page.get_by_placeholder('Enter email')
    input.fill("me@that.site")
    input.clear()
    input.type("me@that.site", delay=100)

    valid_input = page.get_by_label('Valid input').first
    print(valid_input.input_value())


    browser.close()