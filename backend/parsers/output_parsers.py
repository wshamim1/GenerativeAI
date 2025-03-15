from typing import List, Type
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field



class ParserImplementation:
    def __init__(self, parser_class: Type[BaseModel]):
        self.parser_class = parser_class
        self.parser = PydanticOutputParser(pydantic_object=self.parser_class)

    def get_llm_parser(self):
        """Returns the initialized parser."""
        return self.parser