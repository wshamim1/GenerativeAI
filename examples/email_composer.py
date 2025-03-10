
import sys, os
# insert root directory into python module search path
sys.path.insert(1, os.getcwd())

from src.llms.ollama_llm import OllamaLLM
from src.langchain.documentloader.document_loader import DocumentLoader
from src.chains.prompt_chain import GenericPromptChain

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = OllamaLLM().get_llm()

prompt_template  = """you are  helpful assistant. Can you compose me an email to 
                    {person} with agenda {agenda}. 
            """

prompt_chain = GenericPromptChain(llm, prompt_template)

person="Mr X"
agenda = f""" 1. current scope. 
            2. Deployment archtecture. 
              3. future state.
              4. current issues and workaround
                """

response = prompt_chain.run(person=person, agenda=agenda)


print(response)