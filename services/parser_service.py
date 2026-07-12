"""
Parser Service
"""

from models.product import Product


def create_product(
    market: str,
    title: str,
    price: float,
    old_price=None,
    discount=None,
    image_url="",
    product_url="",
    category="",
    campaign_title="",
    start_date="",
    end_date="",
):
    return Product(
        market=market,
        title=title,
        price=price,
        old_price=old_price,
        discount=discount,
        image_url=image_url,
        product_url=product_url,
        category=category,
        campaign_title=campaign_title,
        start_date=start_date,
        end_date=end_date,
    )
