import requests

URL = "https://bim.veesk.net/service/v1.0/home/aktuel"

HEADERS = {
    "Content-Type": "application/json",
    "X-App-version": "20241101"
}


def run():
    response = requests.post(
        URL,
        headers=HEADERS,
        json={"token": ""},
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    products = []

    for section in data["widgets"]["aktuel"]:
        section_name = section["title"]

        for category in section["childs"]:
            category_name = category["title"]

            for product in category["products"]:

                products.append({
                    "sku": product.get("sku"),
                    "name": product.get("title"),
                    "brand": product.get("brands_label"),
                    "category": category_name,
                    "section": section_name,
                    "price": product.get("price"),
                    "special_price": product.get("special_price"),
                    "discount": product.get("discount_percent"),
                    "image": product.get("photo"),
                    "store": "BİM"
                })

    print(f"Toplam {len(products)} ürün bulundu.")

    for product in products[:10]:
        print(product)

    return products
