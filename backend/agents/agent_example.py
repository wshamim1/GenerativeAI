import asyncio
import sys
import os

# Ensure the backend directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from backend.agents.agent_executor import AgentExecutor
from backend.agents.agent_executor1 import AgentExecutor1
from backend.agents.tools.circumference_tool import CircumferenceToolWrapper
from backend.agents.tools.square_tools import SquareToolWrapper
from backend.agents.tools.start_job import StartJobToolWrapper
from backend.agents.tools.weather_tool import WeatherTool
from backend.agents.tools.concat_tool import ConcatToolWrapper
from backend.agents.tools.tavily_search import TavilySearchTool
from typing import List
from pydantic import BaseModel


class ConcatInput(BaseModel):
    items: List[str]

async def main():
    tool_classes = [TavilySearchTool]
    chat_history = []

    

    agent_executor = AgentExecutor(
        llm_name='ollama',  # Change this to 'openai', 'mistral', or 'anthropic' as needed
        model_name='llama3.2',  # Specify the model name
        tool_classes=tool_classes
    )

    # ✅ Ensure `items` is a **valid Python list**
    input_data = "Can you fetch the linked url for  jogi patel. Just give me the linkedin url"

    
    response = agent_executor.run({"input": input_data, "chat_history": chat_history})


    print(response)  # ✅ Should output "aaaa-----bbb"

# Ensure proper asyncio execution
if __name__ == "__main__":
    asyncio.run(main())