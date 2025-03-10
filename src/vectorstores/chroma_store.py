


import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma

load_dotenv()

class VectorStores:

    def __init__(self,documents,embeddings,persist_directory,vector_store_type, search_type):
        self.documents = documents
        self.embeddings = embeddings
        self.persist_directory = persist_directory
        self.vector_store_type = vector_store_type
        self.search_type = search_type

    def store_document(self):
        if self.vector_store_type == 'Chroma':
            vectorstore = Chroma.from_documents(
                documents=self.documents,  # Ensure splited_documents contains valid data
                embedding=self.embeddings,
                persist_directory=self.persist_directory
            )
            vectorstore.persist()
            return "✅ Data successfully stored in ChromaDB!"
        

    def retrive_document(self):

        if self.vector_store_type == 'Chroma':
            vectorstore = Chroma(persist_directory=self.persist_directory, 
                                 embedding_function=self.embeddings)
            
            retriever = vectorstore.as_retriever(search_type=self.search_type)

            return retriever


        