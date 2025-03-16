import asyncio
from langchain.tools import Tool
from dotenv import load_dotenv
import os
from langchain.tools import BaseTool
from typing import List, Type
from pydantic import BaseModel, Field

# Load environment variables from .env file
load_dotenv()

# ✅ Define the Correct Input Schema (List-based)
class ConcatToolInput(BaseModel):
    items: List[str] = Field(description="List of strings to concatenate")

# ✅ Update the Tool to Accept a Single List Instead of Two Separate Arguments
class ConcatTool(BaseTool):
    name: str = "concat_tool"
    description: str = "Concatenates all strings in a given list with '--=========' separator."
    args_schema: Type[BaseModel] = ConcatToolInput
    return_direct: bool = True

    def concat_items(self, items: List[str]) -> str:
        return "--=========".join(items)  # ✅ Concatenate properly

    def _run(self, items: List[str]) -> str:
        return self.concat_items(items)

    async def _arun(self, items: List[str]) -> str:
        return self.concat_items(items)

# ✅ Wrapper to Register the Tool in LangChain
class ConcatToolWrapper:
    def __init__(self):
        self.concating = ConcatTool()
        self.concating_tool = Tool(
            name=self.concating.name,
            func=self.concating._run,
            description=self.concating.description,
            args_schema=self.concating.args_schema
        )

    def get_tool(self):
        return self.concating_tool
