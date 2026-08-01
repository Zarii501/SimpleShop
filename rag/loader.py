import os
import sys
import shutil
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")
django.setup()

from products.models import Product
from langchain_core.documents import Document

products = Product.objects.all()

documents = []

for product in products:

    text = f"""
نام محصول:
{product.name}

دسته بندی:
{product.category.name}

برند:
{product.brand}

قیمت:
{product.price} تومان

موجودی:
{product.inventory}

نوع اتصال:
{product.connectiontype}

رنگ:
{product.color}

گارانتی:
{product.warranty}

"""




    document = Document(

        page_content=text,

        metadata={

            "id": product.id,

            "name": product.name,

            "category": product.category.name,

            "brand": product.brand,

            "price": product.price,

        }

    )

    documents.append(document)