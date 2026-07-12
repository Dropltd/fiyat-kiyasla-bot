import requests

API_URL = "https://www.bim.com.tr/api/bim/home"

def run():
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()

    data = response.json()

    products = []

    for section in data["widgets"]["aktuel"]:
        for child in section.get("childs", []):
            category = child.get("title", "")

            for item in child.get("products", []):
                products.append({
                    "id": item.get("sku"),
                    "name": item.get("title"),
                    "brand": item.get("brands_label"),
                    "category": category,
                    "price": item.get("special_price") or item.get("price"),
                    "normal_price": item.get("price"),
                    "image": item.get("photo"),
                    "store": "BİM",
                })

    print(f"{len(products)} ürün bulundu.")

    return products


if __name__ == "__main__":
    run()
