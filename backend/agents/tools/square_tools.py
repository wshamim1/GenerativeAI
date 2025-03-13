import asyncio
from langchain.tools import Tool
from dotenv import load_dotenv
import os
from langchain.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field, ValidationError
from langchain_core.callbacks import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

# Load environment variables from .env file
load_dotenv()

class SquareToolInput(BaseModel):
    num: int = Field(description="Number to perform square calculation on")  # ✅ Enforced as integer

class SquareTool(BaseTool):
    name: str = "Square calculator"
    description: str = "Use this tool when you need to calculate the square of a given number."
    args_schema: Type[BaseModel] = SquareToolInput  # ✅ Pydantic handles validation
    return_direct: bool = True

    def calculate_square(self, num: int) -> int:
        return int(num) * int(num)  # ✅ Correct square calculation

    def _run(self, num: int) -> int:
        return self.calculate_square(num)  # ✅ Directly use `num`

    async def _arun(self, num: int) -> int:
        await asyncio.sleep(0)  # ✅ Ensure async behavior
        return self.calculate_square(num)

class SquareToolWrapper:
    def __init__(self):
        self.square = SquareTool()
        self.square_tool = Tool(
            name=self.square.name,
            func=self.square._run,  # ✅ Pass `_run` correctly
            description=self.square.description
        )

    def get_tool(self):
        return self.square_tool
