import sys
import os
import json
import re
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
import time
from typing import List

# Load environment variables from .env file
load_dotenv()

# Insert root directory into Python module search path
sys.path.insert(1, os.getcwd())
from backend.llm.generic_llms import GenericLLM
from backend.chains.prompt_templates import GenericPromptChain1
from backend.documentloader.document_loader import DocumentLoader

# Configure LLM
llm_name = 'ollama'  
model_name = 'llama3.1'  
llm = GenericLLM(llm_name, model_name).get_llm()

file_path = "/Users/shamim/Desktop/Codes/GenerativeAI/data/test.pdf"
loader = DocumentLoader(file_path)
doc = loader.load()

# Define a custom Pydantic model
class DocumentSummary(BaseModel):
    summary: str = Field(description="A brief summary of the document")
    words: List[str] = Field(description="A list of interesting words from the document")

PROMPT_TEMPLATE = """
You MUST return a JSON object in the EXACT format below, with no extra text, explanations, or formatting:
{format_instructions}

read the document {document} and summarize and generate me list me 5 words.
"""

prompt_chain = GenericPromptChain1(llm, PROMPT_TEMPLATE, DocumentSummary)

# Run the query
raw_output = prompt_chain.run(document=doc, format_instructions=prompt_chain.parser.get_format_instructions())

# Debug: Print raw output
print("Raw LLM Output:", raw_output)

# Access the attributes of the Pydantic object directly
print("Summary:", raw_output.summary)
print("Words:", raw_output.words)