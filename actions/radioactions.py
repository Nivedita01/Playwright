from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False, slow_mo=500)  # Set headless=True for headless mode
    # Create a new browser page
    page = browser.new_page()
    # Navigate to a webpage
    page.goto("https://bootswatch.com/default")

    radio_option_2 = page.get_by_label('Option two can be something else and selecting it will deselect option one')
    radio_option_2.check()
    radio_option_1 = page.get_by_label('Option one is this and that—be sure to include why it\'s great')   
    radio_option_1.check()

    checkbox = page.get_by_label('Default checkbox')
    checkbox.check()
    print(checkbox.is_checked())
    checkbox.uncheck()
    checkbox.set_checked(True)
    checkbox.set_checked(False)

    switch = page.get_by_label('Default switch checkbox input')
    switch.check()
    switch.uncheck()

    browser.close()