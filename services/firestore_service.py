from firebase_admin import firestore

db = firestore.client()


def save_products(products):
    collection = db.collection("products")

    count = 0

    for product in products:
        sku = product["sku"]

        collection.document(str(sku)).set(product)

        count += 1

    print(f"{count} ürün Firestore'a kaydedildi.")
