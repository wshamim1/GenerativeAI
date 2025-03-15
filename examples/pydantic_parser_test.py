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
from backend.llm.generic_llms import GenericLLM
from backend.documentloader.document_loader import DocumentLoader
from backend.chains.prompt_templates import GenericPromptChain
from backend.parsers.output_parsers import ParserImplementation

# Configure LLM
llm_name = 'ollama'  
model_name = 'deepseek-r1:1.5b'  
llm = GenericLLM(llm_name, model_name).get_llm()
file_path = "/Users/shamim/Desktop/Codes/GenerativeAI/data/test.pdf"
loader = DocumentLoader(file_path)
doc = loader.load()

# Define a custom Pydantic model
class CustomParser(BaseModel):
    summary: str = Field(description="A brief summary of the document")
    words: List[str] = Field(description="A list of interesting facts about the document")


# Initialize the parser implementation with the custom parser class
parser_implementation = ParserImplementation(CustomParser)
parser = parser_implementation.get_llm_parser()





prompt_template = """
You MUST return a JSON object in the EXACT format below, with no extra text, explanations, or formatting:
{format_instructions}

read the document {document} and summarize and generate me list me 5 words.
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=[],  # No dynamic input variables
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Run the query
chain = prompt | llm
raw_output = chain.invoke({"document": doc})  # AIMessage object

# Debug: Print raw output
print("Raw LLM Output:", raw_output)

# Extract text from AIMessage
raw_text = raw_output.content.strip()

# Debug: Print raw output
print("Raw LLM Output:", raw_text)

match = re.search(r"\{.*\}", raw_text, re.DOTALL)
if match:
    json_text = match.group()
else:
    raise ValueError("No valid JSON found in LLM output")

print("=====")

print(json_text)

# Parse JSON correctly
try:
    parsed_output = parser.parse(json_text)
    print("Parsed Output:", parsed_output)
    print("Summary:", parsed_output.summary)
    print("Facts:", parsed_output.words)
except Exception as e:
    print("Parsing Error:", str(e))
    print("Received JSON:", json_text)