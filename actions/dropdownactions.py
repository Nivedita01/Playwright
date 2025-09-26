from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False, slow_mo=500)  # Set headless=True for headless mode
    # Create a new browser page
    page = browser.new_page()
    # Navigate to a webpage
    page.goto("https://bootswatch.com/default")

    dropdown = page.locator("button#btnGroupDrop1")

    dropdown.click()
    page.locator("div.dropdown-menu:visible").highlight()
    page.locator("div.dropdown-menu:visible a:text('Dropdown link')").highlight()
    page.locator("div.dropdown-menu:visible a:text('Dropdown link')").last.highlight()
    dropdown_link = page.locator("div.dropdown-menu:visible a:text('Dropdown link')").last
    dropdown_link.click()


    browser.close()