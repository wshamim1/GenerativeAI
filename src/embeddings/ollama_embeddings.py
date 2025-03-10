


import os
from dotenv import load_dotenv
from langchain_ollama.embeddings import OllamaEmbeddings

load_dotenv()

class OllamaEmbedding:
    def __init__(self):
        embedding_model_name = os.getenv("OLLAMA_EMBEDDINGS_MODEL")
        self.embeddings = OllamaEmbeddings(model=embedding_model_name)

    def get_embeddings(self):
        return self.embeddings



print(OllamaEmbedding().get_embeddings())

