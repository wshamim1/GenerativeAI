import os
from dotenv import load_dotenv
from langchain.tools import BaseTool, Tool
from typing import Type
from pydantic import BaseModel, Field

# Load environment variables from .env file
load_dotenv()

# ✅ Define Input Schema
class AddToolInput(BaseModel):
    a: int = Field(description="The first number")
    b: int = Field(description="The second number")

# ✅ Update the Tool to Accept a Single Dictionary Instead of Separate Arguments
class AddTools(BaseTool):
    name: str = "add_two_numbers"
    description: str = "Adds two numbers and returns the sum."
    args_schema: Type[BaseModel] = AddToolInput  # ✅ Ensuring structured input
    return_direct: bool = True

    def _run(self, a: int, b: int) -> int:
        return a + b + 100  # ✅ Adds 100 for verification

    async def _arun(self, a: int, b: int) -> int:
        return a + b + 100

# ✅ Wrapper to Register the Tool in LangChain
class AddToolsWrapper:
    def __init__(self):
        self.adding = AddTools()
        self.adding_tool = Tool(
            name=self.adding.name,
            func=self.adding._run,
            description=self.adding.description,
            args_schema=self.adding.args_schema  # ✅ Enforce structured input
        )

    def get_tool(self):
        return self.adding_tool
