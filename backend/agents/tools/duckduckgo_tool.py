

from langchain.tools import Tool
from langchain.tools import WikipediaQueryRun
from langchain.utilities import DuckDuckGoSearchAPIWrapper


# API Tool definition
import os
from dotenv import load_dotenv
from langchain.tools import Tool

# Load environment variables from .env file
load_dotenv()

class DuckDuckGoTool:
    def __init__(self):

        duckduckgo = DuckDuckGoSearchAPIWrapper()


        self.duckduckgo_tool = Tool(
            name="DuckDuckGo Search",
            func=duckduckgo.run,
            description="Use this tool when you need to search for real-time information from Google."
        )

    def get_tool(self):
        return self.duckduckgo_tool

