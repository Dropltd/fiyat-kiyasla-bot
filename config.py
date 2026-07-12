"""
Fiyat Kıyasla Bot
Global Configuration
"""

import os

# Firestore Collections
COLLECTION_MARKETS = "market_aktuel"
COLLECTION_NOTIFICATIONS = "notifications"

# Market Sources
BIM_URL = "https://www.bim.com.tr/Categories/100/aktuel-urunler.aspx"

A101_URL = "https://www.a101.com.tr/aldin-aldin"

SOK_URL = "https://www.sokmarket.com.tr/aktuel"

MIGROS_URL = "https://www.migros.com.tr/kampanyalar"

CARREFOUR_URL = "https://www.carrefoursa.com/kampanyalar"

# Request Settings
REQUEST_TIMEOUT = 30

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}

# Environment
SERVICE_ACCOUNT_ENV = "FIREBASE_SERVICE_ACCOUNT"

# Logging
LOG_LEVEL = "INFO"

# Duplicate Control
CHECK_DUPLICATES = True
