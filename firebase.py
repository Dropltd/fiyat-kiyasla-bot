"""
Firebase Firestore Connection
"""

import os
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from config import SERVICE_ACCOUNT_ENV


_db = None


def get_firestore():
    global _db

    if _db is not None:
        return _db

    if not firebase_admin._apps:
        service_account = json.loads(
            os.environ[SERVICE_ACCOUNT_ENV]
        )

        cred = credentials.Certificate(service_account)

        firebase_admin.initialize_app(cred)

    _db = firestore.client()

    return _db
