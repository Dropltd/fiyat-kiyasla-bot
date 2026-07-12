from scraper.bim import run


def main():
    print("=== Fiyat Kıyasla Botu ===")

    products = run()

    print(f"Toplam ürün: {len(products)}")


if __name__ == "__main__":
    main()
