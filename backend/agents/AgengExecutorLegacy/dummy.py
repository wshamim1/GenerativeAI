from langchain.tools import BaseTool
from typing import Union
import asyncio
import sys, os

# Ensure the backend directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from backend.llm.generic_llms import GenericLLM
from langchain.agents import initialize_agent, AgentType

from langchain.tools import BaseTool
from math import pi
from typing import Union
  

class CircumferenceTool(BaseTool):
    name: str = "Circumference calculator"
    description: str = "Use this tool when you need to calculate the circumference of a circle given its radius."

    def _run(self, radius: Union[int, float]) -> float:
        return float(radius) * 2.0 * pi

    async def _arun(self, radius: Union[int, float]) -> float:
        return float(radius) * 2.0 * pi
    

async def main():
    # Initialize an LLM (Modify this part based on your LLM setup)
    llm = GenericLLM("ollama", "llama3.2").get_llm()

    tools = [CircumferenceTool()]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=3,
        early_stopping_method='generate',
    )

    chat_history = []

    response = await agent.ainvoke({"input": "can you calculate the circumference of a circle that has a radius of 7.81mm", "chat_history": chat_history})

    print(f"The response is: {response}")

# Ensure proper asyncio execution
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:  # Handles nested event loops in Jupyter notebooks
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())