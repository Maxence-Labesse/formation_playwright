from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("about:blank")
    
    # Garde le navigateur ouvert pour manipulation manuelle
    input("Appuie sur Entrée pour fermer le navigateur...")
    
    browser.close()