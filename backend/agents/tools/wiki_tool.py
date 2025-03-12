from langchain.tools import Tool
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper


# API Tool definition
import os
from dotenv import load_dotenv
from langchain.tools import Tool

# Load environment variables from .env file
load_dotenv()

class WikiTool:
    def __init__(self):

        wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())





        self.wiki_tool = Tool(
            name="Wikipedia Search",
            func=wiki.run,
            description="Useful for searching Wikipedia articles."
        )

    def get_tool(self):
        return self.wiki_tool

