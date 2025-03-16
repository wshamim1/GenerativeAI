import sys
import os
import asyncio
from pydantic import BaseModel

# Ensure the backend directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from backend.agents.agent_executor1 import AgentExecutor
from backend.agents.tools.maths_tool import AddToolsWrapper  # Ensure the correct import

async def main():
    tool_classes = [AddToolsWrapper]  # Use the correct tool wrapper
    chat_history = []

    agent_executor = AgentExecutor(
        llm_name='ollama',  # Change this to 'openai', 'mistral', or 'anthropic' as needed
        model_name='llama3.1',  # Specify the model name
        tool_classes=tool_classes
    )

    # Provide structured input matching `AddToolInput`
    input_data = {"a": 1, "b": 1}  # Correct input format

    # Run the agent with structured input
    response = agent_executor.run({"input": {"input_variables":input_data}, "chat_history": chat_history})

    print("\nFinal Output:", response)  # Expected output: 102 (1 + 1 + 100)

# Ensure proper asyncio execution
if __name__ == "__main__":
    asyncio.run(main())