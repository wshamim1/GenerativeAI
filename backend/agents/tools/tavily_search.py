# API Tool definition
import os
from dotenv import load_dotenv
from langchain.tools import Tool
from langchain_community.tools import TavilySearchResults

# Load environment variables from .env file
load_dotenv()

class TavilySearchTool:
    def __init__(self):
        serper_api_key = os.getenv('TAVILY_API_KEY')
        if not serper_api_key:
            raise ValueError("TAVILY_API_KEY environment variable is not set.")
        
        self.tavily = TavilySearchResults(serper_api_key=serper_api_key)
        self.tavily_tool = Tool(
            name="Crawl google 2 linkedin profile page",
            func=self.tavily.run,
            description="Use this tool when you need to search for real-time information from Tavily."
        )

    def get_tool(self):
        return self.tavily_tool

# Example usage
if __name__ == "__main__":
    tavily_tool_instance = TavilySearchTool()
    tool = tavily_tool_instance.get_tool()
    print(tool.name)
    print(tool.description)