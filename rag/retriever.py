from rag.vectorstore import get_vector_db


def search(question):

    db = get_vector_db()

    documents = db.similarity_search(
        question,
        k=5
    )

    return documents