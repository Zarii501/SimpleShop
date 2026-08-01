from rag.retriever import search
from rag.prompt_builder import build_prompt
from rag.llm import generate


def ask(question):

    documents = search(question)

    print("="*50)
    print("Documents:", len(documents))
    print("="*50)

    for doc in documents:
        print(doc.metadata["name"])

    if not documents:
        return "این اطلاعات در محصولات فروشگاه موجود نیست."

    prompt = build_prompt(question, documents)

    print("="*50)
    print(prompt)
    print("="*50)

    answer = generate(prompt)

    return answer