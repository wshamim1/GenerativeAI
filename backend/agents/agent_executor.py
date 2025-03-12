# Agent Executor implementation
import os
import importlib
import json
from dotenv import load_dotenv
import sys

# Load environment variables from .env file
load_dotenv()

sys.path.insert(1, os.getcwd())
from langchain.agents import initialize_agent, AgentType
from backend.llm.generic_llms import GenericLLM

class AgentExecutor:
    def __init__(self, llm_name, model_name, tool_classes):
        self.llm_name = llm_name
        self.model_name = model_name
        self.tool_classes = tool_classes
        self.llm = self._initialize_llm()
        self.tools = self._initialize_tools()

    def _initialize_llm(self):
        return GenericLLM(self.llm_name, self.model_name).get_llm()

    def _initialize_tools(self):
        tools = []
        for tool_class in self.tool_classes:
            tool_instance = tool_class()
            tools.append(tool_instance.get_tool())
        return tools

    def run(self, prompt):
        agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True  # Allows the agent to retry when parsing fails
        )
        return agent.run(prompt)

# Example usage
if __name__ == "__main__":
    from backend.agents.tools.search_tool import SearchTool
    # Add more tools as needed
    tool_classes = [SearchTool]

    agent_executor = AgentExecutor(
        llm_name='ollama',  # Change this to 'openai', 'mistral', or 'anthropic' as needed
        model_name='llama3.2',  # Specify the model name
        tool_classes=tool_classes
    )

    response = agent_executor.run("in 2 line tell me about python.")
    print(response)