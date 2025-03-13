import sys, os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# insert root directory into python module search path
sys.path.insert(1, os.getcwd())

from backend.llm.generic_llms import GenericLLM
from backend.documentloader.document_loader import DocumentLoader
from backend.chains.prompt_chain import GenericPromptChain

llm_name = 'ollama'  # Change this to 'openai', 'mistral', or 'anthropic' as needed
model_name = 'llama3.2'  # Specify the model name

llm = GenericLLM(llm_name, model_name).get_llm()

file_path = "/Users/shamim/Desktop/Codes/GenerativeAI/data/linkedin.json"
#for text loader
#loader = DocumentLoader(file_path)

#for json loader
loader = DocumentLoader(file_path, jq_schema=".")
doc = loader.load()

prompt_template = "You are a helpful assistant that reads documents {documents} and " \
        "where all has Eden worked"
prompt_chain = GenericPromptChain(llm, prompt_template)

summary = prompt_chain.run(documents=doc)

print(summary)