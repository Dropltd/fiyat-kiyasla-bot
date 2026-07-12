"""
Fiyat Kıyasla Bot
Main Entry Point
"""

from firebase import get_firestore
from utils.logger import get_logger

logger = get_logger("MarketBot")


def main():
    logger.info("Bot başlatıldı.")

    db = get_firestore()

    logger.info("Firestore bağlantısı başarılı.")

    logger.info("Şimdilik test çalışması tamamlandı.")


if __name__ == "__main__":
    main()
