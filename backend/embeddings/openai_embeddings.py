


import os
from dotenv import load_dotenv
from langchain_openai.embeddings import OpenAIEmbeddings

load_dotenv()

class OllamaEmbedding:
    def __init__(self):
        embedding_model_name = os.getenv("OPENAI_EMBEDDINGS_MODEL")
        self.embeddings = OpenAIEmbeddings(model=embedding_model_name)

    def get_embeddings(self):
        return self.embeddings

print(OllamaEmbedding().get_embeddings())

