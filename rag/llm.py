from ollama import Client

client = Client(
    host="http://localhost:11434"
)


def generate(prompt):

    response = client.generate(
        model="qwen2.5:3b",
        prompt=prompt,
        options={
            "temperature": 0.0,
            "num_predict": 120,
        }
    )

    return response["response"]

