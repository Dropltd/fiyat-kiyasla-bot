"""
Firestore Service
"""

from firebase import get_firestore
from models.product import Product
from utils.helpers import generate_document_id

db = get_firestore()


def save_product(product: Product):

    document_id = generate_document_id(
        f"{product.market}-{product.title}-{product.price}"
    )

    ref = db.collection("market_aktuel").document(document_id)

    if ref.get().exists:
        return False

    ref.set(
        {
            "market": product.market,
            "title": product.title,
            "price": product.price,
            "oldPrice": product.old_price,
            "discount": product.discount,
            "imageUrl": product.image_url,
            "productUrl": product.product_url,
            "category": product.category,
            "campaignTitle": product.campaign_title,
            "startDate": product.start_date,
            "endDate": product.end_date,
            "stock": product.stock,
            "barcode": product.barcode,
            "createdAt": product.created_at,
        }
    )

    return True
