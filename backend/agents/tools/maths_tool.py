import asyncio
import sys
import os
import math
from langchain.tools import Tool
from typing import Union
from langchain.tools import BaseTool

# Ensure the backend directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Define multiple math tools
class MathToolWrapper(BaseTool):
    """A wrapper for multiple math tools."""
    
    @staticmethod
    def square(number: Union[int, float]) -> float:
        return number ** 2

    @staticmethod
    def square_root(number: Union[int, float]) -> float:
        return math.sqrt(number)

    @staticmethod
    def cube(number: Union[int, float]) -> float:
        return number ** 3

    @staticmethod
    def sin(number: Union[int, float]) -> float:
        return math.sin(math.radians(number))

    @staticmethod
    def cos(number: Union[int, float]) -> float:
        return math.cos(math.radians(number))

    def get_tools(self):
        """Return tools for mathematical operations."""
        return [
            Tool(name="Square Calculator", func=lambda x: self.square(float(x)), description="Calculates the square of a number."),
            Tool(name="Square Root Calculator", func=lambda x: self.square_root(float(x)), description="Calculates the square root of a number."),
            Tool(name="Cube Calculator", func=lambda x: self.cube(float(x)), description="Calculates the cube of a number."),
            Tool(name="Sine Calculator", func=lambda x: self.sin(float(x)), description="Calculates the sine of an angle in degrees."),
            Tool(name="Cosine Calculator", func=lambda x: self.cos(float(x)), description="Calculates the cosine of an angle in degrees."),
        ]