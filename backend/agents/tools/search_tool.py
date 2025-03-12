# API Tool definition
import os
from dotenv import load_dotenv
from langchain.tools import Tool
from langchain_community.utilities import GoogleSerperAPIWrapper

# Load environment variables from .env file
load_dotenv()

class SearchTool:
    def __init__(self):
        serper_api_key = os.getenv('SERPER_API_KEY')
        if not serper_api_key:
            raise ValueError("SERPER_API_KEY environment variable is not set.")
        
        self.search = GoogleSerperAPIWrapper(serper_api_key=serper_api_key)
        self.search_tool = Tool(
            name="Google Search",
            func=self.search.run,
            description="Use this tool when you need to search for real-time information from Google."
        )

    def get_tool(self):
        return self.search_tool

# Example usage
if __name__ == "__main__":
    search_tool_instance = SearchTool()
    tool = search_tool_instance.get_tool()
    print(tool.name)
    print(tool.description)