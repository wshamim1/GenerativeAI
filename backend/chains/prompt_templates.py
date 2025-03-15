from typing import List, Type, Dict, Any
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field
import json

class GenericPromptChain:
    def __init__(self, llm, prompt_template):
        self.prompt = ChatPromptTemplate.from_template(prompt_template)
        self.llm = llm
        self.chain = self.prompt | self.llm | StrOutputParser()

    def run(self, **kwargs):
        return self.chain.invoke(kwargs)
    

class GenericPromptChain1:
    def __init__(self, llm, prompt_template: str, parser_class: Type[BaseModel]):
        """Initializes the prompt chain with LLM, template, and parser."""
        self.parser = PydanticOutputParser(pydantic_object=parser_class)
        self.prompt = ChatPromptTemplate.from_template(prompt_template)
        self.llm = llm
        self.chain = self.prompt | self.llm | self.parser

    def run(self, **kwargs):
        """Runs the prompt chain dynamically and returns the Pydantic object."""
        try:
            result = self.chain.invoke(kwargs)
            return result  # Return the Pydantic object directly
        except Exception as e:
            print(f"Error executing prompt chain: {e}")
            return None