import sys
import os
import asyncio
from typing import List
from pydantic import BaseModel

# Ensure the backend directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from backend.agents.agent_executor import AgentExecutor
from backend.agents.tools.weather_tool import WeatherTool  # Ensure this is correctly implemented

# ✅ Define the correct structured input for concatenation


async def main():
    tool_classes = [WeatherTool]  # ✅ Ensure only valid tools are used
    chat_history = []

    agent_executor = AgentExecutor(
        llm_name='ollama',  # Change this to 'openai', 'mistral', or 'anthropic' as needed
        model_name='llama3.1',  # Specify the model name
        tool_classes=tool_classes
    )

    # ✅ Provide structured input matching `ConcatToolInput`
    input_data = "Tell me the weather of New york"

    # ✅ Run the agent with structured input
    response = agent_executor.run({"input": input_data, "chat_history": chat_history})

    print("\nFinal Output:", response)  # ✅ Expected output: "aaaa--=========bbbb"

# Ensure proper asyncio execution
if __name__ == "__main__":
    asyncio.run(main())
