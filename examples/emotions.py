import sys, os
# insert root directory into python module search path
sys.path.insert(1, os.getcwd())

from backend.llm.generic_llms import OllamaLLM
from backend.documentloader.document_loader import DocumentLoader
from backend.chains.prompt_templates import GenericPromptChain

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = OllamaLLM().get_llm()

prompt_template  = """you are emotionally helpful assistant. Classify the sentiments of the user's text with 
            Only one of the following emotions {emotions}. Just generate a single word with emotions"""

prompt_chain = GenericPromptChain(llm, prompt_template)

input="I Like to play Tennis"

response = prompt_chain.run(emotions=input)


print(response)