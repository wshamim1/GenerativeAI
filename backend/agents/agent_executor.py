import asyncio
import os
import sys
import json
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
import importlib
import re
import asyncio

# Ensure the backend directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from backend.llm.generic_llms import GenericLLM

# Load environment variables
load_dotenv()

# Load tool configuration from JSON file
config_path = os.path.join(os.path.dirname(__file__), 'tool_config.json')
with open(config_path, 'r') as config_file:
    TOOL_CLASS_MAP = json.load(config_file)

class AgentExecutor:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools

    @classmethod
    async def create(cls, llm_name, model_name, tool_class_names):
        """Asynchronous factory method to initialize tools properly."""
        llm = GenericLLM(llm_name, model_name).get_llm()
        tools = await cls._initialize_tools_async(tool_class_names)
        return cls(llm, tools)

    @staticmethod
    async def _initialize_tools_async(tool_class_names):
        tasks = [AgentExecutor._create_tool_async(tool_class_name) for tool_class_name in tool_class_names]
        return await asyncio.gather(*tasks)

    @staticmethod
    async def _create_tool_async(tool_class_name):
        if tool_class_name not in TOOL_CLASS_MAP:
            raise ValueError(f"Unsupported tool class: {tool_class_name}")
        
        module_path, class_name = TOOL_CLASS_MAP[tool_class_name].rsplit('.', 1)
        module = importlib.import_module(module_path)
        tool_class = getattr(module, class_name)
        tool_instance = tool_class()

        # ✅ Debugging step: Print loaded tools to verify they exist
        print(f"Loaded tool: {tool_class_name} from {module_path}.{class_name}")

        return tool_instance.get_tool()




    async def run(self, prompt, chat_history=None):
        if chat_history is None:
            chat_history = []

        agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True
        )

        # ✅ Step 1: Get all available tools dynamically
        available_tools = {tool.name.lower(): tool for tool in self.tools}  # Store tools by name

        # ✅ Step 2: Check which tools should be invoked
        sub_queries = []
        for tool_name, tool_instance in available_tools.items():
            if tool_name in prompt.lower():  # Dynamically detect tool mentions
                sub_queries.append((tool_instance, prompt))  # Store tool and query

        # ✅ Step 3: Invoke detected tools dynamically
        if sub_queries:
            tasks = [agent.ainvoke({"input": query, "chat_history": chat_history}) for tool, query in sub_queries]
            responses = await asyncio.gather(*tasks)
            final_response = "\n\n".join(responses)
        else:
            # If no tools match, fallback to normal LLM response
            final_response = await agent.ainvoke({"input": prompt, "chat_history": chat_history})

        print(f"Final response:\n{final_response}")
        return final_response