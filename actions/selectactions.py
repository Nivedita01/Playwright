from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False, slow_mo=500)  # Set headless=True for headless mode
    # Create a new browser page
    page = browser.new_page()
    # Navigate to a webpage
    page.goto("https://bootswatch.com/default")

    select = page.get_by_label('Example select')
    select.select_option('2')

    multi_select = page.get_by_label('Example multiple select')
    multi_select.select_option(['1', '3', '4'])

    browser.close()