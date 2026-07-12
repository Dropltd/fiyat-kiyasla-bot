from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
            "https://www.bim.com.tr/categories/100/aktuel-urunler.aspx",
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(5000)

        print("=" * 50)
        print("CURRENT URL:")
        print(page.url)
        print("=" * 50)

        html = page.content()

        print("=" * 50)
        print("HTML START")
        print(html[:5000])
        print("HTML END")
        print("=" * 50)

        browser.close()

    return []
