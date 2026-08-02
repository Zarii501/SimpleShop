import os
import sys
import django
from django.apps import apps as django_apps

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if not django_apps.ready:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")
    django.setup()

from products.models import Product
from langchain_core.documents import Document


def build_document(product):
    """ساخت متن قابل embed برای یک محصول (برای استفاده در ایندکس اولیه و sync لحظه‌ای)"""
    text = f"""نام محصول: {product.name}
دسته‌بندی: {product.category.name}
برند: {product.brand}
قیمت: {product.price} تومان
موجودی: {product.inventory}
نوع اتصال: {product.connectiontype}
رنگ: {product.color}
گارانتی: {product.warranty}
توضیحات: {product.description}
"""
    return Document(
        page_content=text,
        metadata={
            "id": product.id,
            "name": product.name,
            "category": product.category.name,
            "brand": product.brand,
            "price": product.price,
        }
    )


def load_all_documents():
    products = Product.objects.select_related("category").all()
    return [build_document(p) for p in products]


documents = load_all_documents()