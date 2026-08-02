from rag.retriever import search
from rag.prompt_builder import build_prompt
from rag.llm import generate

DEBUG = True


def ask(question):
    documents = search(question)

    if DEBUG:
        print("=" * 50)
        print("Relevant documents:", len(documents))
        for doc in documents:
            print("-", doc.metadata["name"])
        print("=" * 50)

    if not documents:
        return "این اطلاعات در محصولات فروشگاه موجود نیست."

    prompt = build_prompt(question, documents)

    if DEBUG:
        print(prompt)
        print("=" * 50)

    answer = generate(prompt)
    return answer