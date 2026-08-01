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

from langchain_community.vectorstores import Chroma
from .embedding import embedding_model


def get_vector_db():

    return Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model
    )