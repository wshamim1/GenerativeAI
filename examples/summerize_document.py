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

file_path = "/Users/shamim/Desktop/Codes/GenerativeAI/data/test.pdf"
loader = DocumentLoader(file_path)
doc = loader.load()

prompt_template = "You are a helpful assistant that reads documents {documents} and summarize in 1 line."
prompt_chain = GenericPromptChain(llm, prompt_template)

summary = prompt_chain.run(documents=doc)

print(summary)