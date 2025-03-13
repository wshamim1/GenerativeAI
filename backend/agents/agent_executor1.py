

import os
import importlib
import json
from dotenv import load_dotenv
import sys

# Load environment variables from .env file
load_dotenv()

sys.path.insert(1, os.getcwd())
from langchain.agents import initialize_agent, AgentType, AgentExecutor, create_react_agent
from backend.llm.generic_llms import GenericLLM

from langchain import hub


class AgentExecutor1:
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
        react_prompt = hub.pull("hwchase17/react")

        agent = create_react_agent(
            tools=self.tools,
            llm=self.llm,
            prompt=react_prompt
        )
        agent_executor = AgentExecutor(agent=agent, tools=self.tools, verbose=True)
        return agent_executor.invoke(prompt)

    pass

