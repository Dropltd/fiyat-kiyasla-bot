"""
BİM Scraper
"""

import requests
from bs4 import BeautifulSoup

from config import BIM_URL, HEADERS, REQUEST_TIMEOUT
from utils.logger import get_logger

logger = get_logger("BIM")


class BimScraper:

    def __init__(self):
        self.url = BIM_URL

    def fetch_page(self):

        logger.info("BİM sayfası indiriliyor...")

        response = requests.get(
            self.url,
            headers=HEADERS,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.text

    def parse(self):

        html = self.fetch_page()

        soup = BeautifulSoup(html, "lxml")

        logger.info("HTML başarıyla alındı.")

        # TODO
        # Gerçek ürün ayrıştırma kodu buraya eklenecek.
        # Şimdilik boş liste döndür.

        return []

    def run(self):

        logger.info("BİM Scraper başladı.")

        products = self.parse()

        logger.info(
            f"{len(products)} ürün bulundu."
        )

        return products
