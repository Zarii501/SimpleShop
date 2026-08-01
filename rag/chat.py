from rag.service import ask

while True:

    question = input("سؤال: ")

    if question == "exit":
        break

    print()

    print(ask(question))

    print()