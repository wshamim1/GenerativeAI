from src.llms.ollama_llm import OllamaLLM
from src.langchain.documentloader.document_loader import DocumentLoader
from src.chains.prompt_chain import GenericPromptChain

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = OllamaLLM().get_llm()

file_path = "/Users/shamim/Desktop/Codes/GenerativeAI/data/test.csv"
loader = DocumentLoader(file_path)
doc = loader.load()

prompt_template = "You are a helpful assistant that reads documents {documents} and tell me the ID for ccc."
prompt_chain = GenericPromptChain(llm, prompt_template)

summary = prompt_chain.run(documents=doc)


print(summary)