from scraper.bim import run
from services.firestore_service import save_products


def main():
    print("=== Fiyat Kıyasla Botu ===")

    products = run()

    print(f"{len(products)} ürün çekildi.")

    save_products(products)

    print("İşlem tamamlandı.")


if __name__ == "__main__":
    main()
