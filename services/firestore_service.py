import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate(
        json.loads(os.environ["FIREBASE_CREDENTIALS"])
    )
    firebase_admin.initialize_app(cred)

db = firestore.client()


def save_products(products):
    collection = db.collection("products")

    count = 0

    for product in products:
        sku = product["sku"]
        collection.document(str(sku)).set(product)
        count += 1

    print(f"{count} ürün Firestore'a kaydedildi.")
