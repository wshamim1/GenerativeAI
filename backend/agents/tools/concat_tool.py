import asyncio
from langchain.tools import Tool
from dotenv import load_dotenv
import os
from langchain.tools import BaseTool
from typing import List, Type
from pydantic import BaseModel, Field
from langchain_core.callbacks import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

# Load environment variables from .env file
load_dotenv()

class ConcatToolInput(BaseModel):
    items: List[str] = Field(description="List of strings to concatenate")

class ConcatTool(BaseTool):
    name: str = "Concat all items"
    description: str = "Use this tool when you need to concatenate all strings in a given list."
    args_schema: Type[BaseModel] = ConcatToolInput  # Removed trailing comma
    return_direct: bool = True

    def concat_items(self, items: List[str]) -> str:
        return "-----====---".join(items)  # Ensure correct list joining

    def _run(self, items: List[str]) -> str:
        return self.concat_items(items)

    async def _arun(self, items: List[str]) -> str:
        await asyncio.sleep(0)  # Ensure async behavior
        return self.concat_items(items)

class ConcatToolWrapper:
    def __init__(self):
        self.concating = ConcatTool()
        self.concating_tool = Tool(
            name=self.concating.name,
            func=self.concating._run,
            description=self.concating.description,
            args_schema=self.concating.args_schema  # Properly set args_schema
        )

    def get_tool(self):
        return self.concating_tool