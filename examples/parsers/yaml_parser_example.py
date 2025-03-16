import sys
import os
import re
import json
import time
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain.output_parsers import YamlOutputParser
from langchain_core.prompts import PromptTemplate
from typing import List

# Load environment variables from .env file
load_dotenv()

# Insert root directory into Python module search path
sys.path.insert(1, os.getcwd())

# Import necessary modules
from backend.llm.generic_llms import GenericLLM
from backend.documentloader.document_loader import DocumentLoader
from backend.chains.prompt_templates import GenericPromptChain1

# Configure LLM
llm_name = 'ollama'  
model_name = 'llama3.1'  
llm = GenericLLM(llm_name, model_name).get_llm()

# Load document
file_path = "/Users/shamim/Desktop/Codes/GenerativeAI/data/test.pdf"
loader = DocumentLoader(file_path)
doc = loader.load()

# Define a custom Pydantic model for structured output
class CustomParser(BaseModel):
    summary: str = Field(description="A brief summary of the document")
    words: List[str] = Field(description="A list of 5 words extracted from the document")

# Initialize the YAML output parser with the custom Pydantic model
parser = YamlOutputParser(pydantic_object=CustomParser)

# Corrected prompt: Expect YAML output, not JSON
prompt_template = """
You MUST return a YAML object in the EXACT format below, with no extra text, explanations, or formatting:
{format_instructions}

Read the document and:
1. Summarize it in a concise paragraph.
2. Extract and list 5 key words from the document.

Document:
{document}
"""

# Create a prompt template with dynamic variables
prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["document"],  # Dynamic input variable
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Run the LLM chain
chain = prompt | llm
raw_output = chain.invoke({"document": doc})  # AIMessage object

# Debug: Print raw output
print("Raw LLM Output:", raw_output)

# Extract content from AIMessage
raw_text = raw_output.content.strip()

# Debug: Print cleaned output
print("\n==== Raw LLM Response ====\n", raw_text)

# Extract valid YAML content using regex
match = re.search(r"```yaml\n(.*?)\n```", raw_text, re.DOTALL)
if match:
    yaml_text = match.group(1)
else:
    yaml_text = raw_text  # Fallback if code block markers are not present

# Debug: Print extracted YAML text
print("\n==== Extracted YAML ====\n", yaml_text)

# Parse YAML correctly
try:
    parsed_output = parser.parse(yaml_text)
    print("\n==== Parsed Output ====\n", parsed_output)
    print("\nSummary:", parsed_output.summary)
    print("\nKey Words:", parsed_output.words)
except Exception as e:
    print("\nParsing Error:", str(e))
    print("\nReceived YAML:", yaml_text)
