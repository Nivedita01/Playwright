from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False, slow_mo=500)  # Set headless=True for headless mode
    # Create a new browser page
    page = browser.new_page()
    # Navigate to a webpage
    page.goto("https://playwright.dev/python")

    # Locate a link element with "Docs" and click it
    docs_link = page.get_by_role('link', name='Docs')
    docs_link.click()

    #Get the URL of the current page
    print("Docs:", page.url)

    browser.close()

