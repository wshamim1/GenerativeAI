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
                    Generate me a 10 line stories for title {title}. 
                    """

prompt_chain = GenericPromptChain(llm, prompt_template)

title="Lion and fox"

response = prompt_chain.run(title=title)


print(response)