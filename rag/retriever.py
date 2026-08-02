from rag.vectorstore import get_vector_db

TOP_K = 5
SIMILARITY_THRESHOLD = 0.45


def search(question):
    db = get_vector_db()
    results = db.similarity_search_with_score(question, k=TOP_K)

    relevant_documents = []
    for doc, distance in results:
        print(f"[retriever] {doc.metadata.get('name')} -> distance={distance:.4f}")
        if distance <= SIMILARITY_THRESHOLD:
            relevant_documents.append(doc)

    return relevant_documents