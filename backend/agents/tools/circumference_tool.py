from langchain.tools import Tool
from dotenv import load_dotenv
import os
from langchain.tools import BaseTool
from typing import Union
from math import pi

# Load environment variables from .env file
load_dotenv()

class CircumferenceTool(BaseTool):
    name: str = "Circumference calculator"
    description: str = "Use this tool when you need to calculate the circumference of a circle given its radius."

    def _run(self, radius: Union[int, float,str]) -> float:
        return float(radius) * 2.0 * pi

    async def _arun(self, radius: Union[int, float,str]) -> float:
        return float(radius) * 2.0 * pi

class CircumferenceToolWrapper:
    def __init__(self):
        self.circumference = CircumferenceTool()
        self.circumference_tool = Tool(
            name=self.circumference.name,
            func=self.circumference._run,
            description=self.circumference.description
        )

    def get_tool(self):
        return self.circumference_tool