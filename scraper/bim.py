from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
    "https://www.bim.com.tr/categories/100/aktuel-urunler.aspx",
    wait_until="networkidle",
    timeout=60000
)

html = page.content()
        )

        html = page.content()

        with open("page.html", "w", encoding="utf-8") as f:
            f.write(html)

        print(html[:5000])

        browser.close()

    return []
