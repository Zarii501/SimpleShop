from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
)

vector = embedding_model.embed_query(
    "کیبورد مناسب برنامه نویسی"
)
