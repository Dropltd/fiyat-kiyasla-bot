"""
Fiyat Kıyasla Bot
Main
"""

from scraper.bim import BimScraper
from services.firestore_service import save_product
from utils.logger import get_logger

logger = get_logger("MAIN")


def run_bim():

    logger.info("BİM taraması başlıyor...")

    scraper = BimScraper()

    products = scraper.run()

    saved = 0

    for product in products:

        if save_product(product):
            saved += 1

    logger.info(f"Kaydedilen ürün sayısı : {saved}")


def main():

    logger.info("Bot çalışmaya başladı.")

    run_bim()

    logger.info("Bot tamamlandı.")


if __name__ == "__main__":
    main()
