"""
Product Model
Tüm marketlerden gelen ürünler bu modele dönüştürülür.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    market: str
    title: str
    price: float

    old_price: Optional[float] = None
    discount: Optional[int] = None

    image_url: str = ""
    product_url: str = ""

    category: str = ""

    campaign_title: str = ""

    start_date: str = ""
    end_date: str = ""

    stock: bool = True

    barcode: str = ""

    created_at: str = ""
