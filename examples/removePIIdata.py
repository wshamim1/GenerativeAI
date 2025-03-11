import sys, os
# insert root directory into python module search path
sys.path.insert(1, os.getcwd())

from backend.llms.ollama_llm import OllamaLLM
from backend.documentloader.document_loader import DocumentLoader
from backend.chains.prompt_chain import GenericPromptChain

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = OllamaLLM().get_llm()

prompt_template  = """you are  helpful assistant. 
                    Remove all PII data from the text {input_txt}. 
                    """

prompt_chain = GenericPromptChain(llm, prompt_template)

input_txt="My name is tst. My phone number is 9002219092. My address is 545 tst street, Palms spring, CA, 18999"

response = prompt_chain.run(input_txt=input_txt)


print(response)