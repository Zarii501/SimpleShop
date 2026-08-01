import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "shop.settings"
)

django.setup()

from rag.loader import documents
from rag.embedding import embedding_model
from langchain_community.vectorstores import Chroma

DB_PATH = "chroma_db"

try:

    vector_db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding_model
    )

    # حذف همه داده‌های قبلی
    vector_db.delete_collection()

    # ساخت Collection جدید
    vector_db = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=DB_PATH
    )

    print("Vector Database Updated.")

except Exception as e:
    print(e)