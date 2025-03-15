

import sys, os
# insert root directory into python module search path
sys.path.insert(1, os.getcwd())

from backend.llm.generic_llms import OllamaLLM
from backend.documentloader.document_loader import DocumentLoader
from backend.chains.prompt_templates import GenericPromptChain
from backend.vectorstores.chroma_store import VectorStores
from backend.embeddings.ollama_embeddings import OllamaEmbedding

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

llm = OllamaLLM().get_llm()

file_path = "/Users/shamim/Desktop/Codes/GenerativeAI/data/test.csv"
loader = DocumentLoader(file_path)
doc = loader.load()


embeddings = OllamaEmbedding().get_embeddings()

persist_directory = "/Users/shamim/Desktop/Codes/GenerativeAI/vectorDBs"


retriver =  VectorStores(documents='', embeddings=embeddings, persist_directory=persist_directory, 
                         vector_store_type='Chroma',search_type='similarity').retrive_document()
qa = RetrievalQA.from_chain_type(llm=llm, 
                                 chain_type="stuff", 
                                 retriever=retriver, 
                                 return_source_documents=True)


# ---- Define Prompt Template ---- #
PROMPT_TEMPLATE = """Human: You are an AI assistant providing fact-based answers using statistical information where possible.
Use the following context to answer the question enclosed in <question> tags.
If you don't know the answer, say that you don't know; don't make up an answer.

<context>
{context}
</context>

<question>
{question}
</question>

Provide specific responses with statistics or numbers when available.

Assistant:"""

prompt = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["context", "question"])
# ---- Format Retrieved Documents ---- #

rag_chain = (
    {"context": retriver , "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# ---- Run Query ---- #
query = "summarize"
response = rag_chain.invoke(query)

# ---- Print Response ---- #
print(response)
