import sys, os
# insert root directory into python module search path
sys.path.insert(1, os.getcwd())

from src.llms.ollama_llm import OllamaLLM
from src.langchain.documentloader.document_loader import DocumentLoader
from src.chains.prompt_chain import GenericPromptChain

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = OllamaLLM().get_llm()

prompt_template  = """you are emotionally helpful assistant. Classify the sentiments of the user's text with 
            Only one of the following emotions {emotions}. Just generate a single word with emotions"""

prompt_chain = GenericPromptChain(llm, prompt_template)

input="I Like to play Tennis"

response = prompt_chain.run(emotions=input)


print(response)