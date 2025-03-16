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
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True  # Allows the agent to retry when parsing fails
        )
        return agent.invoke(prompt)

