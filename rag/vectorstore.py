import os
import sys
import django
from django.apps import apps as django_apps

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if not django_apps.ready:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")
    django.setup()

from langchain_community.vectorstores import Chroma
from .embedding import embedding_model

PERSIST_DIRECTORY = os.path.join(BASE_DIR, "chroma_db")
COLLECTION_NAME = "products"


def get_vector_db():
    return Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embedding_model,
        collection_name=COLLECTION_NAME,
        collection_metadata={"hnsw:space": "cosine"},
    )


def upsert_product(product):
    """آپدیت/اضافه کردن یک محصول در vectorstore بدون دست زدن به بقیه رکوردها"""
    from rag.loader import build_document

    db = get_vector_db()
    doc_id = str(product.id)
    document = build_document(product)

    try:
        db.delete(ids=[doc_id])
    except Exception:
        pass  

    db.add_documents([document], ids=[doc_id])


def delete_product(product_id):
    """حذف یک محصول از vectorstore وقتی از دیتابیس اصلی حذف می‌شه"""
    db = get_vector_db()
    try:
        db.delete(ids=[str(product_id)])
    except Exception:
        pass