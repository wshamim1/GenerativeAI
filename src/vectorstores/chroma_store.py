import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma, ElasticVectorSearch
from langchain_community.vectorstores.elastic import ElasticSearch  # Assuming this exists
from langchain_community.vectorstores.pinecone import Pinecone  # Assuming this exists
from langchain_community.vectorstores.mongodb import MongoDB  # Assuming this exists

load_dotenv()

class VectorStores:
    
    def __init__(self, documents=None, embeddings=None, persist_directory=None, 
                 vector_store_type="", search_type=""):
        self.documents = documents
        self.embeddings = embeddings
        self.persist_directory = persist_directory
        self.vector_store_type = vector_store_type
        self.search_type = search_type

    def store_document(self):
        # Store document depending on the vector store type
        if self.vector_store_type == 'Chroma':
            vectorstore = Chroma.from_documents(
                documents=self.documents, 
                embedding=self.embeddings,
                persist_directory=self.persist_directory
            )
            vectorstore.persist()
            return "✅ Data successfully stored in ChromaDB!"
        
        elif self.vector_store_type == 'ElasticSearch':
            # Assuming ElasticSearch vector store
            vectorstore = ElasticSearch.from_documents(
                documents=self.documents,
                embedding=self.embeddings,
                persist_directory=self.persist_directory
            )
            vectorstore.persist()
            return "✅ Data successfully stored in ElasticSearch!"
        
        elif self.vector_store_type == 'Pinecone':
            # Assuming Pinecone vector store
            vectorstore = Pinecone.from_documents(
                documents=self.documents,
                embedding=self.embeddings,
                persist_directory=self.persist_directory
            )
            vectorstore.persist()
            return "✅ Data successfully stored in Pinecone!"
        
        elif self.vector_store_type == 'MongoDB':
            # Assuming MongoDB vector store
            vectorstore = MongoDB.from_documents(
                documents=self.documents,
                embedding=self.embeddings,
                persist_directory=self.persist_directory
            )
            vectorstore.persist()
            return "✅ Data successfully stored in MongoDB!"
        
        else:
            raise ValueError(f"Unsupported vector store type: {self.vector_store_type}")
        

    def retrieve_document(self):
        # Retrieve document depending on the vector store type
        if self.vector_store_type == 'Chroma':
            vectorstore = Chroma(persist_directory=self.persist_directory, embedding_function=self.embeddings)
            retriever = vectorstore.as_retriever(search_type=self.search_type)
            return retriever
        
        elif self.vector_store_type == 'ElasticSearch':
            vectorstore = ElasticSearch(persist_directory=self.persist_directory, embedding_function=self.embeddings)
            retriever = vectorstore.as_retriever(search_type=self.search_type)
            return retriever
        
        elif self.vector_store_type == 'Pinecone':
            vectorstore = Pinecone(persist_directory=self.persist_directory, embedding_function=self.embeddings)
            retriever = vectorstore.as_retriever(search_type=self.search_type)
            return retriever
        
        elif self.vector_store_type == 'MongoDB':
            vectorstore = MongoDB(persist_directory=self.persist_directory, embedding_function=self.embeddings)
            retriever = vectorstore.as_retriever(search_type=self.search_type)
            return retriever
        
        else:
            raise ValueError(f"Unsupported vector store type: {self.vector_store_type}")

# Example Usage:
if __name__ == '__main__':
    # Assuming documents and embeddings are already defined
    documents = ["Document 1", "Document 2"]  # Example documents
    embeddings = "your_embeddings"  # Example embedding model
    persist_directory = "your_directory"
    vector_store_type = 'Chroma'  # Can be 'Chroma', 'ElasticSearch', 'Pinecone', or 'MongoDB'
    search_type = 'similarity'  # Example search type
    
    # Initialize VectorStores class
    vectorstore = VectorStores(documents, embeddings, persist_directory, vector_store_type, search_type)
    
    # Store document
    store_message = vectorstore.store_document()
    print(store_message)
    
    # Retrieve document
    retriever = vectorstore.retrieve_document()
    print(retriever)  # The retriever object
