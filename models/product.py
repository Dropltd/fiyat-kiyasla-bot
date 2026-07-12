from dataclasses import dataclass

@dataclass
class Product:

    market: str
    title: str
    price: float

    old_price: float | None = None

    discount: int | None = None

    image: str = ""

    product_url: str = ""

    category: str = ""

    start_date: str = ""

    end_date: str = ""
