from langchain.tools import Tool
from dotenv import load_dotenv
import os
from langchain.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field
from langchain_core.callbacks import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

# Load environment variables from .env file
load_dotenv()

class StartJobInput(BaseModel):
    job_id: str = Field(description="Job ID")

class StartJobTool(BaseTool):
    name: str = "Start job"
    description: str = "Use this tool when you need to Start Streamsets Job."
    args_schema: Type[BaseModel] = StartJobInput  # ✅ Fixed the type annotation
    return_direct: bool = True

    def start_job(self, job_id: str) -> str:
        return f"Hello, your job with Job ID {job_id} started successfully."

    def _run(self, job_id: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        return self.start_job(job_id)

    async def _arun(self, job_id: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        return await self._run(job_id, run_manager=run_manager)

class StartJobToolWrapper:
    def __init__(self):
        self.job = StartJobTool()
        self.start_job_tool = Tool(
            name=self.job.name,
            func=self.job._run,
            description=self.job.description
        )

    def get_tool(self):
        return self.start_job_tool
