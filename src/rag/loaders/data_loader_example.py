

import sys, os
# insert root directory into python module search path
sys.path.insert(1, os.getcwd())

from src.llms.ollama_llm import OllamaLLM
from src.documentloader.document_loader import DocumentLoader
from src.splitter.document_splitter import DocumentsSplitter
from src.embeddings.ollama_embeddings import OllamaEmbedding
from src.vectorstores.chroma_store import VectorStores



llm = OllamaLLM().get_llm()

file_path = "/Users/shamim/Desktop/Codes/GenerativeAI/data/test.csv"
loader = DocumentLoader(file_path)
doc = loader.load()

splited_document = DocumentsSplitter(document=doc).split_document()

print(splited_document)

embeddings = OllamaEmbedding().get_embeddings()

persist_directory = "/Users/shamim/Desktop/Codes/GenerativeAI/vectorDBs"

resp = VectorStores(documents=splited_document, embeddings=embeddings, persist_directory=persist_directory, vector_store_type='Chroma',search_type='similarity').store_document()

print(resp)