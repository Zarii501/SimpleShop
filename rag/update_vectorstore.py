import os
import sys
import django
from django.apps import apps as django_apps

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if not django_apps.ready:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")
    django.setup()

from rag.loader import load_all_documents
from rag.embedding import embedding_model
from rag.vectorstore import PERSIST_DIRECTORY, COLLECTION_NAME, get_vector_db
from langchain_community.vectorstores import Chroma


def rebuild():
    documents = load_all_documents()
    ids = [str(doc.metadata["id"]) for doc in documents]

    db = get_vector_db()
    try:
        db.delete_collection()
    except Exception:
        pass

    Chroma.from_documents(
        documents=documents,
        ids=ids,
        embedding=embedding_model,
        persist_directory=PERSIST_DIRECTORY,
        collection_name=COLLECTION_NAME,
        collection_metadata={"hnsw:space": "cosine"},
    )
    print(f"Vector Database Rebuilt with {len(documents)} products.")


if __name__ == "__main__":
    rebuild()