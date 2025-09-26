from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False, slow_mo=500)  # Set headless=True for headless mode
    # Create a new browser page
    page = browser.new_page()
    # Navigate to a webpage
    page.goto("https://bootswatch.com/default")

    textarea = page.get_by_label("Example textarea")

    textarea.fill("This is a sample text.")
    textarea.clear()
    textarea.press("KeyW")
    textarea.press("KeyA")
    textarea.press("Shift+KeyA")
    textarea.press("Control+ArrowLeft")

    browser.close()